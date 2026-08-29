import pygame
import math
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

center_x = WINDOW_WIDTH / 2
center_y = WINDOW_HEIGHT / 2

sim_5_big_circle_radius = 270
sim_5_balls = []
sim_5_num_balls = 400
sim_5_launch_vel = 3
for i in range(sim_5_num_balls):
    sim_5_balls.append({"x": WINDOW_WIDTH / 2 - sim_5_num_balls / 2 + i, "y": 100, "vert_vel": sim_5_launch_vel, "hor_vel": 0, "color": random.choice([(255,0,0), (0,0,255)]), "bounced": False, "bounce_timer": 0})
sim_5_small_radius = 4

def halfcircle_collision_check(circle_radius, ball_x, ball_y):
    distance = math.sqrt((ball_x - WINDOW_WIDTH / 2) ** 2 + (ball_y - WINDOW_HEIGHT / 2) ** 2)
    if distance < circle_radius + 8 and distance > circle_radius - 8 and ball_y >= WINDOW_HEIGHT / 2:
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

def sim_5(screen):
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

def sim_5_reset():
    global sim_5_big_circle_radius, sim_5_balls, sim_5_num_balls, sim_5_launch_vel, sim_5_small_radius
    sim_5_big_circle_radius = 270
    sim_5_balls = []
    sim_5_num_balls = 400
    sim_5_launch_vel = 3
    for i in range(sim_5_num_balls):
        sim_5_balls.append({"x": WINDOW_WIDTH / 2 - sim_5_num_balls / 2 + i, "y": 100, "vert_vel": sim_5_launch_vel, "hor_vel": 0, "color": random.choice([(255,0,0), (0,0,255)]), "bounced": False, "bounce_timer": 0})
    sim_5_small_radius = 4