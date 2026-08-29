import pygame
import math


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

center_x = WINDOW_WIDTH / 2
center_y = WINDOW_HEIGHT / 2

sim_1_circle_pos = [WINDOW_WIDTH / 2, 200]
sim_1_circle_radius = 20
sim_1_circle_hor_vel = 20
sim_1_circle_vert_vel = 35
sim_1_gravity = 0.4
sim_1_bounce_absorb = 0.9
sim_1_friction = 0.995

def sim_1(screen):
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
    pygame.draw.circle(screen, (0,255,0), tuple(sim_1_circle_pos), sim_1_circle_radius)

def sim_1_reset():
    global sim_1_circle_pos, sim_1_circle_radius, sim_1_circle_hor_vel, sim_1_circle_vert_vel, sim_1_gravity, sim_1_bounce_absorb, sim_1_friction
    sim_1_circle_pos = [WINDOW_WIDTH / 2, 200]
    sim_1_circle_radius = 20
    sim_1_circle_hor_vel = 20
    sim_1_circle_vert_vel = 35
    sim_1_gravity = 0.4
    sim_1_bounce_absorb = 0.9
    sim_1_friction = 0.995