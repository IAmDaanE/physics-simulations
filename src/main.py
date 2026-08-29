import pygame
import random
import math
from sim_1 import sim_1, sim_1_reset
from sim_2 import sim_2, sim_2_reset
from sim_3 import sim_3, sim_3_reset
from sim_4 import sim_4, sim_4_reset
from sim_5 import sim_5, sim_5_reset
from sim_6 import sim_6, sim_6_reset

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

center_x = WINDOW_WIDTH / 2
center_y = WINDOW_HEIGHT / 2

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Physics Simulation")
clock = pygame.time.Clock()

sim_1_img = pygame.transform.scale_by(pygame.image.load("../icons/sim_1_icon.png"), 0.2)
sim_2_img = pygame.transform.scale_by(pygame.image.load("../icons/sim_2_icon.png"), 0.195)
sim_3_img = pygame.transform.scale_by(pygame.image.load("../icons/sim_3_icon.png"), 0.193)
sim_4_img = pygame.transform.scale_by(pygame.image.load("../icons/sim_4_icon.png"), 0.199)
sim_5_img = pygame.transform.scale_by(pygame.image.load("../icons/sim_5_icon.png"), 0.2)
sim_6_img = pygame.transform.scale_by(pygame.image.load("../icons/sim_6_icon.png"), 0.2)

running = True
left_mouse_clicked = False
pos = 0
current_screen = "homescreen"

sim_1_rect = pygame.Rect(27, 81, 231, 178)
sim_2_rect = pygame.Rect(sim_1_rect.right + 27, 81, 231, 178)
sim_3_rect = pygame.Rect(sim_2_rect.right + 27, 81, 231, 178)
sim_4_rect = pygame.Rect(27, 340, 231, 178)
sim_5_rect = pygame.Rect(sim_1_rect.right + 27, 340, 231, 178)
sim_6_rect = pygame.Rect(sim_2_rect.right + 27, 340, 231, 178)

def display_homescreen():
    global current_screen, pos, left_mouse_clicked, sim_1_circle_vert_vel, sim_1_circle_hor_vel, sim_2_launch_speed
    if left_mouse_clicked and sim_1_rect.collidepoint(pos):
        current_screen = "sim_1"
    if left_mouse_clicked and sim_2_rect.collidepoint(pos):
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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            left_mouse_clicked = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            current_screen = "homescreen"
            sim_1_reset()
            sim_2_reset()
            sim_3_reset()
            sim_4_reset()
            sim_5_reset()
            sim_6_reset()
    if current_screen == "homescreen":
        display_homescreen()
    if current_screen == "sim_1":
        sim_1(screen)
    if current_screen == "sim_2":
        sim_2(screen)
    if current_screen == "sim_3":
        sim_3(screen)
    if current_screen == "sim_4":
        sim_4(screen)
    if current_screen == "sim_5":
        sim_5(screen)
    if current_screen == "sim_6":
        sim_6(screen)

    left_mouse_clicked = False
        
    pygame.display.update()
    clock.tick(60)