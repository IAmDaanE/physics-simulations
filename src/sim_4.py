import pygame
import math
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

center_x = WINDOW_WIDTH / 2
center_y = WINDOW_HEIGHT / 2

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
sim_4_friction = 0.998

def rect_bounce(vel_1, vel_2, size_1, size_2):
    new_v1 = ((size_1 - size_2)/(size_1 + size_2)) * vel_1 + ((2 * size_2)/(size_1 + size_2)) * vel_2
    new_v2 = ((2 * size_1)/(size_1 + size_2)) * vel_1 + ((size_2 - size_1)/(size_1 + size_2)) * vel_2
    return new_v1, new_v2

def sim_4(screen):
    global sim_4_rect_1_rect, sim_4_rect_1_vel, sim_4_rect_2_rect, sim_4_rect_2_vel
    screen.fill((255,255,255))

    sim_4_rect_1_rect.x += sim_4_rect_1_vel
    sim_4_rect_2_rect.x += sim_4_rect_2_vel

    if sim_4_rect_1_vel == 0:
        sim_4_rect_1_vel = 0.0001
    if sim_4_rect_2_vel == 0:
        sim_4_rect_2_vel = 0.0001

    sim_4_rect_1_vel *= sim_4_friction
    sim_4_rect_2_vel *= sim_4_friction

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

def sim_4_reset():
    global sim_4_rect_1_mass, sim_4_rect_2_mass, sim_4_rect_1_size, sim_4_rect_2_size, sim_4_rect_1_rect, sim_4_rect_2_rect, sim_4_rect_1_vel, sim_4_rect_2_vel, sim_4_friction
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
    sim_4_friction = 0.998