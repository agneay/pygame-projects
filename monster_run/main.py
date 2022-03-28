import pygame
import sys

if __name__ == "__main__":
    pygame.init()

resolution = (800,400)
icon = pygame.image.load("monster.png")
screen  = pygame.display.set_mode(resolution)
pygame.display.set_caption("monster run")
pygame.display.set_icon(icon)
is_run = True
sky_color = (52, 235, 225)
fps = 60
Clock = pygame.time.Clock()
sky = pygame.image.load("graphics/Sky.png")
ground = pygame.image.load("graphics/ground.png")

def destroy_game():
    pygame.quit()
    is_run = False
    sys.exit()

while is_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            destroy_game()
        if event.type  == pygame.KEYDOWN:
            if event.key == pygame.K_q or pygame.K_ESCAPE:
                destroy_game()
    
    screen.fill(sky_color)
    screen.blit(sky,(0,0))
    screen.blit(ground,(0,300))
    Clock.tick(fps)
    pygame.display.update()