import pygame
import math
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

center_x = WINDOW_WIDTH / 2
center_y = WINDOW_HEIGHT / 2

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

def sim_6(screen):
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

def sim_6_reset():
    global sim_6_circle_radius, sim_6_offset, sim_6_small_side, sim_6_colors, sim_6_trail_1, sim_6_trail_2, sim_6_trail_3, sim_6_orbital_radius, sim_6_gravity_strength, sim_6_start_vel, sim_6_balls
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