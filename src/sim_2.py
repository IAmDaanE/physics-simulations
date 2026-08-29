import pygame
import math
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

center_x = WINDOW_WIDTH / 2
center_y = WINDOW_HEIGHT / 2

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

def sim_2(screen):
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

def sim_2_reset():
    global sim_2_balls, sim_2_big_radius, sim_2_big_vert_vel, sim_2_big_hor_vel, sim_2_big_pos, sim_2_big_gravity, sim_2_gravity, sim_2_bounce_absorb, sim_2_friction, sim_2_exploded, sim_2_radius, sim_2_launch_speed_range, sim_2_num_balls
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