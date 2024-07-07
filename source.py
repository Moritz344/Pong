import pygame
import random
import time


x = 800
y = 600
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("pong")
clock = pygame.time.Clock()

# game variablen
player_pos_x = 200
player_pos_y = 300
player_speed = 7

player_x_2 = 600
player_y_2 = 300
player_speed_2 = 14

ball_size = 10
ball_pos_x = x // 2
ball_pos_y = player_pos_y // 2
ball_speed_x = 5
ball_speed_y = 5

# Score System
score_1 = 0
score_2 = 0

# sfx
pygame.init()
paddle = pygame.mixer.Sound("paddle.mp3")
wall = pygame.mixer.Sound("wall.mp3")
score = pygame.mixer.Sound("score.mp3")

# TEXT
pygame.font.init()
font = pygame.font.SysFont("Minecraft", 50)
text_farbe = (255, 255, 255)

# farben
weiss = (255, 255, 255)
dark_grey = (0, 0, 0)
blue = (15, 82, 186)

# Retro Neon
dark_blue = (0, 0, 139)
neon_grün = (57, 255, 20)
neon_pink = (255, 20, 147)

# Weltraum
black = (0, 0, 0)
sternen_weiß = (237, 237, 237)
glow_blue = (30, 144, 255)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.update()
            run = False

    screen.fill(dark_blue)

    player = pygame.draw.rect(screen, neon_grün, [player_pos_x, player_pos_y, 10, 50])
    # print("x:", player_pos_x, "y:", player_pos_y)
    player_2 = pygame.draw.rect(screen, neon_grün, [player_x_2, player_y_2, 10, 50])

    ball = pygame.draw.ellipse(screen, weiss, [ball_pos_x, ball_pos_y, ball_size, ball_size])

    def func_netz():
       for i in range(10,600,40):
           pygame.draw.rect(screen,weiss,(x // 2,i,5,20)) 

    # ball collision with objects
    if ball_pos_x < 0 or ball_pos_x > x:
        ball_speed_x *= -1
        score.play()
    if ball_pos_y < 0 or ball_pos_y > y:
        wall.play()
        ball_speed_y *= -1

    if ball_pos_x < 0:
        score_2 += 1
        print("Punkt für Spieler_2:", score_2)
    elif ball_pos_x > x:
        score_1 += 1
        print("Punkt für Spieler 1:", score_1)
    
    if score_1 == 10 or score_2 == 10:
        print("Round over!")
        score_1 = 0
        score_2 = 0
    
    # drawing the Text
    def drawing_text():
        text_surface = font.render(f"{score_1}", False, (255, 255, 255))
        text_surface_2 = font.render(f"{score_2}", False, (255, 255, 255))

        screen.blit(text_surface, (200, 0))
        screen.blit(text_surface_2, (600, 0))

    # ball collision with player
    def ball_collision():  
        global ball_speed_x,ball_pos_x,ball_pos_y
        if ball.colliderect(player):
            ball_speed_x = -ball_speed_x
            paddle.play() 

        elif ball.colliderect(player_2):
            ball_speed_x = -ball_speed_x
            paddle.play() 

        ball_pos_y += ball_speed_y
        ball_pos_x += ball_speed_x

       # print(ball_pos_x, ball_pos_y)

    # Keyboard Input
    def keyboard_input():
        global player_pos_y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos_y -= player_speed
        elif keys[pygame.K_s]:
            player_pos_y += player_speed

    # collision Player 1
    def paddle_collision():
        global player_pos_y
        if player_pos_y < 0:
            player_pos_y = 0
        elif player_pos_y > 560:
            player_pos_y = 560

    
   
   
    # Player_2
    def paddle_2_controls():
        global ball_pos_y,player_y_2
        easy_mode = 2
        medium_mode = 4.8
        hard_mode = 5 

        if ball_pos_y > player_y_2:
            player_y_2 += medium_mode 
        elif ball_pos_y < player_y_2:
            player_y_2 -= medium_mode 

    if __name__ == "__main__":
        ball_collision()
        paddle_collision()
        paddle_2_controls()
        keyboard_input()
        drawing_text()
        func_netz()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()