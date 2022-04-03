import pygame
import sys
import random
import time

if __name__ == "__main__":
    pygame.init()

# variables
screen_width = 800
screen_height = 400
resolution = (screen_width,screen_height)
start_time = 0
is_run = True
fps = 60
Clock = pygame.time.Clock()
player_gravity = 0
game_state = True
middle_screen = (screen_width//2,screen_height//2)

#colors
sky_color = (52, 235, 225)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,255,0)
green = (0,0,255)

#fonts
default_font = pygame.font.Font(None,50)
default_font2 = pygame.font.Font(None,150)

#text
game_over_text = default_font2.render("Game Over !!",False,white)
resume_text = default_font.render("To resume press SPACE ",False,white)

#Images 
sky = pygame.image.load("graphics/Sky.png")
ground = pygame.image.load("graphics/ground.png")
snail1 = pygame.image.load("graphics/snail/snail1.png")
snail2 = pygame.image.load("graphics/snail/snail2.png")
Fly1 = pygame.image.load("graphics/Fly/Fly1.png")
Fly2 = pygame.image.load("graphics/Fly/Fly2.png")
player = pygame.image.load("graphics/Player/player_stand.png")
icon = pygame.image.load("monster.png")

#positions
snail_y = 300
snail_x = 750
player_rect = player.get_rect(midbottom = (100,300))
snail1_rect = snail1.get_rect(midbottom = (snail_x,snail_y))
game_over_text_rect = game_over_text.get_rect(midtop = (screen_width/2,0))
resume_text_rect = resume_text.get_rect(center = (screen_width//2+30,screen_height//2+150))

#window controlls
screen  = pygame.display.set_mode(resolution)
pygame.display.set_caption("monster run")
pygame.display.set_icon(icon)


def destroy_game():
    print("Game quit..")
    pygame.quit()
    is_run = False
    sys.exit()

def score_handle():
    current_time = pygame.time.get_ticks()//1000 - start_time
    text = default_font.render("Score:"+str(current_time),False,black)
    text_rect  = text.get_rect(topright = (800,0))
    screen.blit(text,text_rect)

def game_over_screen():
    screen.fill(black)
    screen.blit(game_over_text,game_over_text_rect)
    player_big = pygame.transform.scale2x(player)
    player_big_rect = player_big.get_rect(center = middle_screen)
    screen.blit(player_big,player_big_rect)
    screen.blit(resume_text,resume_text_rect)

while is_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            destroy_game()
        if event.type  == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                destroy_game()
        if game_state: 
            if event.type == pygame.KEYDOWN:   
                if event.key == pygame.K_SPACE and player_rect.bottom >300:
                    player_gravity = -20
                if event.key == pygame.K_q:
                    destroy_game()
            if event.type == pygame.MOUSEBUTTONDOWN and (player_rect.bottom > 300):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = True
                    snail1_rect.left = 800
    if game_state:
        screen.fill(sky_color)

        screen.blit(sky,(0,0))
        screen.blit(ground,(0,300))
        screen.blit(snail1,snail1_rect)
        screen.blit(player,player_rect)
        score_handle()

        snail1_rect.x -= 5

        if snail1_rect.x < -40:
            snail1_rect.x = 750

        player_gravity+=1
        player_rect.y+=player_gravity
        if player_rect.y > 220:
            player_rect.y = 220
    else:
        game_over_screen()

    if snail1_rect.colliderect(player_rect):
        game_state = False
        start_time = pygame.time.get_ticks()//1000
        
    
    Clock.tick(fps)
    pygame.display.update()