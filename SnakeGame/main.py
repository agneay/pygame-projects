import pygame
import random
import time

pygame.init()

color = (16, 176, 59)
is_run = True
resolution = (640,428)
icon = pygame.image.load("logo.png")
apple = pygame.image.load("apple.png")
backgruond = pygame.image.load("background.jpg")

applex = random.randint(0,500)
appley = random.randint(0,700)

screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Snake Game")
pygame.display.set_icon(icon)

def apple_origin(x,y):
    screen.blit(apple,(x,y))

while is_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_run = False

    screen.fill(color)
    screen.blit(backgruond,(0,0))
    apple_origin(applex,appley)
    pygame.display.update()
