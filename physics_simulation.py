import pygame
import random
import math

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

center_x = WINDOW_WIDTH / 2
center_y = WINDOW_HEIGHT / 2

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Physics Simulation")
clock = pygame.time.Clock()

#-----------images----------
sim_1_img = pygame.transform.scale_by(pygame.image.load("sim_1_icon.png"), 0.2)
sim_2_img = pygame.transform.scale_by(pygame.image.load("sim_2_icon.png"), 0.195)
sim_3_img = pygame.transform.scale_by(pygame.image.load("sim_3_icon.png"), 0.193)
sim_4_img = pygame.transform.scale_by(pygame.image.load("sim_4_icon.png"), 0.199)
sim_5_img = pygame.transform.scale_by(pygame.image.load("sim_5_icon.png"), 0.2)
sim_6_img = pygame.transform.scale_by(pygame.image.load("sim_6_icon.png"), 0.2)

#--------general_vars--------
running = True
left_mouse_clicked = False
pos = 0
current_screen = "homescreen"

#--------homescreen_vars-----
sim_1_rect = pygame.Rect(27, 81, 231, 178)
sim_2_rect = pygame.Rect(sim_1_rect.right + 27, 81, 231, 178)
sim_3_rect = pygame.Rect(sim_2_rect.right + 27, 81, 231, 178)
sim_4_rect = pygame.Rect(27, 340, 231, 178)
sim_5_rect = pygame.Rect(sim_1_rect.right + 27, 340, 231, 178)
sim_6_rect = pygame.Rect(sim_2_rect.right + 27, 340, 231, 178)

#--------sim_1_vars--------
sim_1_circle_pos = [WINDOW_WIDTH / 2, 200]
sim_1_circle_radius = 20
sim_1_circle_hor_vel = 20
sim_1_circle_vert_vel = 35
sim_1_gravity = 0.4
sim_1_bounce_absorb = 0.9
sim_1_friction = 0.995

#---------sim_2_vars-------
sim_2_balls = []
sim_2_big_radius = 30
sim_2_big_vert_vel = -10
sim_2_big_hor_vel = 10
sim_2_big_pos = [50, 300]
sim_2_big_gravity = 0.3
sim_2_gravity = 0.4
sim_2_bounce_absorb = 0.9
sim_2_friction = 0.995
sim_2_exploded = False
sim_2_radius = 10
sim_2_launch_speed_range = [15, 35]
sim_2_num_balls = 400

#---------sim_3_vars-------
sim_3_balls = []
sim_3_exploded = False
sim_3_counter = 0
sim_3_explosion_time = 37
sim_3_start = 60
sim_3_big_radius = 250
sim_3_small_radius = 12
sim_3_movement_speed = 10
sim_3_center = [WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2]
sim_3_growth_radius = 0.2
sim_3_increasing = False
sim_3_accelaration = 0.5
sim_3_launch_speed = 5
sim_3_timer = 0

#---------sim_4_vars-------
sim_4_rect_1_mass = 50
sim_4_rect_2_mass = 1
if sim_4_rect_1_mass > sim_4_rect_2_mass:
    sim_4_rect_1_size = 80
    sim_4_rect_2_size = 40
elif sim_4_rect_2_mass > sim_4_rect_1_mass:
    sim_4_rect_1_size = 40
    sim_4_rect_2_size = 80
else:
    sim_4_rect_1_size = 60
    sim_4_rect_2_size = 60
sim_4_rect_1_rect = pygame.Rect(60, WINDOW_HEIGHT - sim_4_rect_1_size, sim_4_rect_1_size, sim_4_rect_1_size)
sim_4_rect_2_rect = pygame.Rect(WINDOW_WIDTH - sim_4_rect_2_size - 60, WINDOW_HEIGHT - sim_4_rect_2_size, sim_4_rect_2_size, sim_4_rect_2_size)
sim_4_rect_1_vel = 10
sim_4_rect_2_vel = -5

#---------sim_5_vars-------
sim_5_big_circle_radius = 270
sim_5_balls = []
sim_5_num_balls = 400
sim_5_launch_vel = 3
for i in range(sim_5_num_balls):
    sim_5_balls.append({"x": WINDOW_WIDTH / 2 - sim_5_num_balls / 2 + i, "y": 100, "vert_vel": sim_5_launch_vel, "hor_vel": 0, "color": random.choice([(255,0,0), (0,0,255)]), "bounced": False, "bounce_timer": 0})
sim_5_small_radius = 2

#---------sim_6_vars-------
sim_6_circle_radius = 13
sim_6_offset = 200
sim_6_small_side = sim_6_offset / math.sqrt(2)
sim_6_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
sim_6_trail_1 = []
sim_6_trail_2 = []
sim_6_trail_3 = []
sim_6_orbital_radius = 280
sim_6_gravity_strength = 600
side = sim_6_orbital_radius * math.sqrt(3)
sim_6_start_vel = math.sqrt(sim_6_gravity_strength / side)
sim_6_balls = [
    {
        "x": center_x + sim_6_orbital_radius * math.cos(math.radians(90)),
        "y": center_y - sim_6_orbital_radius * math.sin(math.radians(90)),
        "hor_vel": sim_6_start_vel,
        "vert_vel": 0
    },
    {
        "x": center_x + sim_6_orbital_radius * math.cos(math.radians(210)),
        "y": center_y - sim_6_orbital_radius * math.sin(math.radians(210)),
        "hor_vel": sim_6_start_vel * math.cos(math.radians(210 - 90)),
        "vert_vel": -sim_6_start_vel * math.sin(math.radians(210 - 90))
    },
    {
        "x": center_x + sim_6_orbital_radius * math.cos(math.radians(330)),
        "y": center_y - sim_6_orbital_radius * math.sin(math.radians(330)),
        "hor_vel": sim_6_start_vel * math.cos(math.radians(330 - 90)),
        "vert_vel": -sim_6_start_vel * math.sin(math.radians(330 - 90))
    }
]

def ball_collision_check(ball_1_x, ball_1_y, ball_2_x, ball_2_y, radius):
    dx = abs(ball_1_x - ball_2_x)
    dy = abs(ball_1_y - ball_2_y)
    if dx*dx + dy*dy < (radius * 2) ** 2:
        return True
    else:
        return False
    
def bounce(ball1_hv, ball1_vv, ball2_hv, ball2_vv):
    return ball2_hv, ball2_vv, ball1_hv, ball1_vv 

def rect_bounce(vel_1, vel_2, size_1, size_2):
    new_v1 = ((size_1 - size_2)/(size_1 + size_2)) * vel_1 + ((2 * size_2)/(size_1 + size_2)) * vel_2
    new_v2 = ((2 * size_1)/(size_1 + size_2)) * vel_1 + ((size_2 - size_1)/(size_1 + size_2)) * vel_2
    return new_v1, new_v2

def halfcircle_collision_check(circle_radius, ball_x, ball_y):
    distance = math.sqrt((ball_x - WINDOW_WIDTH / 2) ** 2 + (ball_y - WINDOW_HEIGHT / 2) ** 2)
    if distance < circle_radius + 8 and distance > circle_radius - 8 and ball_y >= WINDOW_HEIGHT / 2:
        print("blhbkhbkjhbkjhbk")
        return True
    else:
        return False
    
def halfcircle_bounce(ball_x, ball_y, hor_vel, vert_vel):
    local_angle = round((ball_x - 130) / 3)

    nx = -math.cos(math.radians(local_angle))
    ny = math.sin(math.radians(local_angle))
    
    dot = hor_vel * nx + vert_vel * ny
    new_vx = hor_vel - 2 * dot * nx
    new_vy = vert_vel - 2 * dot * ny
    
    return new_vx, new_vy

#------------------------------------------------------------------------------------------------------------------------------------------

def display_homescreen():
    global current_screen, pos, left_mouse_clicked, sim_1_circle_vert_vel, sim_1_circle_hor_vel, sim_2_launch_speed
    if left_mouse_clicked and sim_1_rect.collidepoint(pos):
        current_screen = "sim_1"
        #sim_1_circle_hor_vel = random.randint(-200, 200)
        #sim_1_circle_vert_vel = random.randint(-200, 200)
        #sim_1_circle_hor_vel = int(input("Enter the horizontal launch velocity: "))
        #sim_1_circle_vert_vel = int(input("Enter the vertical launch velocity: "))
    if left_mouse_clicked and sim_2_rect.collidepoint(pos):
        #sim_2_launch_speed = int(input("Enter the launch speed: "))
        current_screen = "sim_2"
    if left_mouse_clicked and sim_3_rect.collidepoint(pos):
        current_screen = "sim_3"
    if left_mouse_clicked and sim_4_rect.collidepoint(pos):
        current_screen = "sim_4"
    if left_mouse_clicked and sim_5_rect.collidepoint(pos):
        current_screen = "sim_5"
    if left_mouse_clicked and sim_6_rect.collidepoint(pos):
        current_screen = "sim_6"

    screen.fill((255,255,255))
    screen.blit(sim_1_img, sim_1_rect.topleft)
    screen.blit(sim_2_img, sim_2_rect.topleft)
    screen.blit(sim_3_img, sim_3_rect.topleft)
    screen.blit(sim_4_img, sim_4_rect.topleft)
    screen.blit(sim_5_img, sim_5_rect.topleft)
    screen.blit(sim_6_img, sim_6_rect.topleft)
    pygame.draw.rect(screen, (0,0,0), sim_1_rect, 1)
    pygame.draw.rect(screen, (0,0,0), sim_2_rect, 1)
    pygame.draw.rect(screen, (0,0,0), sim_3_rect, 1)
    pygame.draw.rect(screen, (0,0,0), sim_4_rect, 1)
    pygame.draw.rect(screen, (0,0,0), sim_5_rect, 1)
    pygame.draw.rect(screen, (0,0,0), sim_6_rect, 1)

def sim_1():
    global sim_1_circle_hor_vel, sim_1_circle_vert_vel, sim_1_circle_pos, sim_1_circle_radius, sim_1_bounce_absorb, sim_1_friction, sim_1_gravity
    sim_1_circle_pos[0] += sim_1_circle_hor_vel
    sim_1_circle_pos[1] += sim_1_circle_vert_vel

    if sim_1_circle_pos[0] + sim_1_circle_radius >= WINDOW_WIDTH:
        sim_1_circle_pos[0] = WINDOW_WIDTH - sim_1_circle_radius - 1
        sim_1_circle_hor_vel *= -1
        sim_1_circle_hor_vel *= sim_1_bounce_absorb

    if sim_1_circle_pos[0] - sim_1_circle_radius <= 0:
        sim_1_circle_pos[0] = sim_1_circle_radius + 1
        sim_1_circle_hor_vel *= -1
        sim_1_circle_hor_vel *= sim_1_bounce_absorb

    if sim_1_circle_pos[1] + sim_1_circle_radius >= WINDOW_HEIGHT:
        sim_1_circle_pos[1] = WINDOW_HEIGHT - sim_1_circle_radius
        sim_1_circle_vert_vel *= -1
        if abs(sim_1_circle_vert_vel) > sim_1_bounce_absorb * 2:
            sim_1_circle_vert_vel *= sim_1_bounce_absorb
        else:
            sim_1_friction = 0.9

    if sim_1_circle_pos[1] - sim_1_circle_radius <= 0:
        sim_1_circle_pos[1] = sim_1_circle_radius + 1
        sim_1_circle_vert_vel *= -1
        sim_1_circle_vert_vel *= sim_1_bounce_absorb

    sim_1_circle_vert_vel += sim_1_gravity
    sim_1_circle_vert_vel *= sim_1_friction

    sim_1_circle_hor_vel *= sim_1_friction
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0,0,255), tuple(sim_1_circle_pos), sim_1_circle_radius)

def sim_2():
    global sim_2_exploded, sim_2_big_vert_vel, sim_2_big_hor_vel, sim_2_friction
    screen.fill((255,255,255))
    if not sim_2_exploded:
        sim_2_big_pos[0] += sim_2_big_hor_vel
        sim_2_big_pos[1] += sim_2_big_vert_vel
        sim_2_big_vert_vel += sim_2_big_gravity
        if sim_2_big_pos[0] + sim_2_big_radius >= WINDOW_WIDTH:
            sim_2_exploded = True
            for i in range(sim_2_num_balls):
                x = sim_2_big_pos[0]
                y = sim_2_big_pos[1]
                dir = random.randint(90, 270)
                launch_speed = random.randint(sim_2_launch_speed_range[0], sim_2_launch_speed_range[1])
                hor_vel = launch_speed * math.cos(math.radians(dir))
                vert_vel = launch_speed * math.sin(math.radians(dir))
                sim_2_balls.append({"x": x, "y": y, "hor_vel": hor_vel, "vert_vel": vert_vel})
    else:
        for ball in sim_2_balls:
            ball["x"] += ball["hor_vel"]
            ball["y"] += ball["vert_vel"]

            if ball["x"] + sim_2_radius >= WINDOW_WIDTH:
                ball["x"] = WINDOW_WIDTH - sim_2_radius - 1
                ball["hor_vel"] *= -1
                ball["hor_vel"] *= sim_2_bounce_absorb

            if ball["x"] - sim_2_radius <= 0:
                ball["x"] = sim_2_radius + 1
                ball["hor_vel"] *= -1
                ball["hor_vel"] *= sim_2_bounce_absorb

            if ball["y"] + sim_2_radius >= WINDOW_HEIGHT:
                ball["y"] = WINDOW_HEIGHT - sim_2_radius
                ball["vert_vel"] *= -1
                if abs(ball["vert_vel"]) > sim_2_bounce_absorb * 2:
                    ball["vert_vel"] *= sim_2_bounce_absorb

            if ball["y"] - sim_2_radius <= 0:
                ball["y"] = sim_2_radius + 1
                ball["vert_vel"] *= -1
                ball["vert_vel"] *= sim_2_bounce_absorb

            ball["vert_vel"] += sim_2_gravity
            ball["vert_vel"] *= sim_2_friction

            ball["hor_vel"] *= sim_2_friction

            pygame.draw.circle(screen, (0, 100, 255), (ball["x"], ball["y"]), sim_2_radius)
    
    if not sim_2_exploded:
        pygame.draw.circle(screen, (255, 0, 0), tuple(sim_2_big_pos), sim_2_big_radius)

def sim_3():

    global sim_3_balls, sim_3_center, sim_3_big_radius, sim_3_growth_radius, sim_3_exploded, sim_3_increasing, sim_3_timer

    screen.fill((255,255,255))
    sim_3_timer += 1
    
    if sim_3_timer > sim_3_explosion_time and not sim_3_exploded:
        for i in range(50):
                dir = random.randint(0, 360)
                hor_vel = sim_3_launch_speed * math.cos(math.radians(dir))
                vert_vel = sim_3_launch_speed * math.sin(math.radians(dir))
                x = sim_3_center[0] + math.cos(math.radians(dir)) * sim_3_big_radius
                y = sim_3_center[1] + math.sin(math.radians(dir)) * sim_3_big_radius
                sim_3_balls.append({"x": x, "y": y, "hor_vel": hor_vel, "vert_vel": vert_vel, "dir": dir})
        sim_3_exploded = True

    sim_3_growth_radius += sim_3_accelaration

    if not sim_3_increasing:
        sim_3_big_radius -= sim_3_growth_radius
        if sim_3_big_radius < 5:
            sim_3_increasing = True
    else:
        sim_3_big_radius += sim_3_growth_radius

    for ball in sim_3_balls:
        ball["x"] += ball["hor_vel"]
        ball["y"] += ball["vert_vel"]

    for ball in sim_3_balls:
        if ball["x"] - sim_3_small_radius <= 0:
            ball["hor_vel"] *= -1
            ball["x"] = sim_3_small_radius
        if ball["y"] - sim_3_small_radius <= 0:
            ball["vert_vel"] *= -1
            ball["y"] = sim_3_small_radius
        if ball["x"] + sim_3_small_radius >= WINDOW_WIDTH:
            ball["hor_vel"] *= -1
            ball["x"] = WINDOW_WIDTH - sim_3_small_radius
        if ball["y"] + sim_3_small_radius >= WINDOW_HEIGHT:
            ball["vert_vel"] *= -1
            ball["y"] = WINDOW_HEIGHT - sim_3_small_radius

    for i, ball1 in enumerate(sim_3_balls):
        for ball2 in sim_3_balls[i+1:]:
            if ball_collision_check(ball1["x"], ball1["y"], ball2["x"], ball2["y"], sim_3_small_radius):
                ball1["hor_vel"], ball1["vert_vel"], ball2["hor_vel"], ball2["vert_vel"] = bounce(ball1["hor_vel"], ball1["vert_vel"], ball2["hor_vel"], ball2["vert_vel"])
                
                dx = ball1["x"] - ball2["x"]
                dy = ball1["y"] - ball2["y"]
                dist = math.sqrt(dx*dx + dy*dy)
                overlap = (2 * sim_3_small_radius) - dist

                if dist == 0:
                    dist = 0.01

                nx = dx / dist
                ny = dy / dist
                ball1["x"] += nx * overlap / 2
                ball1["y"] += ny * overlap / 2
                ball2["x"] -= nx * overlap / 2
                ball2["y"] -= ny * overlap / 2

    if not sim_3_exploded:
        pygame.draw.circle(screen, (0, 0, 255), (sim_3_center[0], sim_3_center[1]), sim_3_big_radius)

    for ball in sim_3_balls:
        pygame.draw.circle(screen, (255, 0, 0), (ball["x"], ball["y"]), sim_3_small_radius)
    
def sim_4():
    global sim_4_rect_1_rect, sim_4_rect_1_vel, sim_4_rect_2_rect, sim_4_rect_2_vel
    screen.fill((255,255,255))

    sim_4_rect_1_rect.x += sim_4_rect_1_vel
    sim_4_rect_2_rect.x += sim_4_rect_2_vel

    if sim_4_rect_1_vel == 0:
        sim_4_rect_1_vel = 0.0001
    if sim_4_rect_2_vel == 0:
        sim_4_rect_2_vel = 0.0001

    #print(sim_4_rect_1_vel)
    #print(sim_4_rect_2_vel)

    if sim_4_rect_1_rect.x <= 0:
        sim_4_rect_1_rect.x = 0
        sim_4_rect_1_vel *= -1
    if sim_4_rect_2_rect.x <= 0:
        sim_4_rect_2_rect.x = 0
        sim_4_rect_2_vel *= -1
    if sim_4_rect_1_rect.x >= WINDOW_WIDTH - sim_4_rect_1_size:
        sim_4_rect_1_rect.x = WINDOW_WIDTH - sim_4_rect_1_size - 1
        sim_4_rect_1_vel *= -1
    if sim_4_rect_2_rect.x >= WINDOW_WIDTH - sim_4_rect_2_size:
        sim_4_rect_2_rect.x = WINDOW_WIDTH - sim_4_rect_2_size - 1
        sim_4_rect_2_vel *= -1

    if sim_4_rect_1_rect.colliderect(sim_4_rect_2_rect):
        if sim_4_rect_1_rect.x < sim_4_rect_2_rect.x:
            sim_4_rect_1_rect.right = sim_4_rect_2_rect.x + 1
        else:
            sim_4_rect_2_rect.right = sim_4_rect_1_rect.x + 1
        sim_4_rect_1_vel, sim_4_rect_2_vel = rect_bounce(sim_4_rect_1_vel, sim_4_rect_2_vel, sim_4_rect_1_mass, sim_4_rect_2_mass)
    
    pygame.draw.rect(screen, (255, 0, 0), sim_4_rect_1_rect)
    pygame.draw.rect(screen, (0, 0, 255), sim_4_rect_2_rect)

def sim_5():
    global sim_5_balls
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,0,0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), sim_5_big_circle_radius, 2)
    pygame.draw.rect(screen, (255,255,255), (0,0, WINDOW_WIDTH, WINDOW_HEIGHT / 2))

    for ball in sim_5_balls:
        ball["x"] += ball["hor_vel"]
        ball["y"] += ball["vert_vel"]

    for ball in sim_5_balls:
        pygame.draw.circle(screen, ball["color"], (ball["x"], ball["y"]), sim_5_small_radius)

    for ball in sim_5_balls:
        if not ball["bounced"]:
            if halfcircle_collision_check(sim_5_big_circle_radius, ball["x"], ball["y"]):
                ball["hor_vel"], ball["vert_vel"] = halfcircle_bounce(ball["x"], ball["y"], ball["hor_vel"], ball["vert_vel"])
                ball["y"] -= 2
                ball["bounced"] = True
                ball["bounce_timer"] = 5
        else:
            ball["bounce_timer"] -= 1
            if ball["bounce_timer"] == 0:
                ball["bounced"] = False

def sim_6():
    screen.fill((255, 255, 255))

    for i, ball1 in enumerate(sim_6_balls):
        for j, ball2 in enumerate(sim_6_balls):
            if i == j:
                continue
            else:
                distance_x = ball2["x"] - ball1["x"]
                distance_y = ball2["y"] - ball1["y"]
                distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
                rel_angle = math.atan2(distance_y, distance_x)
                force = sim_6_gravity_strength / (distance  / 2) ** 2
                ball1["hor_vel"] += math.cos(rel_angle) * force
                ball1["vert_vel"] += math.sin(rel_angle) * force

    for ball in sim_6_balls:
        ball["x"] += ball["hor_vel"]
        ball["y"] += ball["vert_vel"]

    sim_6_trail_1.append((sim_6_balls[0]["x"], sim_6_balls[0]["y"]))
    sim_6_trail_2.append((sim_6_balls[1]["x"], sim_6_balls[1]["y"]))
    sim_6_trail_3.append((sim_6_balls[2]["x"], sim_6_balls[2]["y"]))

    if len(sim_6_trail_1) > 2:
        pygame.draw.aalines(screen, (sim_6_colors[0]), False, sim_6_trail_1)
        pygame.draw.aalines(screen, (sim_6_colors[1]), False, sim_6_trail_2)
        pygame.draw.aalines(screen, (sim_6_colors[2]), False, sim_6_trail_3)

    ball_counter = 0
    for ball in sim_6_balls:
        pygame.draw.circle(screen, sim_6_colors[ball_counter], (ball["x"], ball["y"]), sim_6_circle_radius)
        ball_counter += 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            left_mouse_clicked = True
    if current_screen == "homescreen":
        display_homescreen()
    if current_screen == "sim_1":
        sim_1()
    if current_screen == "sim_2":
        sim_2()
    if current_screen == "sim_3":
        sim_3()
    if current_screen == "sim_4":
        sim_4()
    if current_screen == "sim_5":
        sim_5()
    if current_screen == "sim_6":
        sim_6()
        
    pygame.display.update()
    clock.tick(60)