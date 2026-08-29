import pygame
import math
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

center_x = WINDOW_WIDTH / 2
center_y = WINDOW_HEIGHT / 2

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

def ball_collision_check(ball_1_x, ball_1_y, ball_2_x, ball_2_y, radius):
    dx = abs(ball_1_x - ball_2_x)
    dy = abs(ball_1_y - ball_2_y)
    if dx*dx + dy*dy < (radius * 2) ** 2:
        return True
    else:
        return False
    
def bounce(ball1_hv, ball1_vv, ball2_hv, ball2_vv):
    return ball2_hv, ball2_vv, ball1_hv, ball1_vv 

def sim_3(screen):

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

def sim_3_reset():
    global sim_3_balls, sim_3_exploded, sim_3_counter, sim_3_explosion_time, sim_3_start, sim_3_big_radius, sim_3_small_radius, sim_3_movement_speed, sim_3_center, sim_3_growth_radius, sim_3_increasing, sim_3_accelaration, sim_3_launch_speed, sim_3_timer
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