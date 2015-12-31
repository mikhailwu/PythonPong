import pygame
from dashedLine import *

pygame.init()
screen = pygame.display.set_mode((500, 300))
done = False
is_blue = True

#player1 constants
pX1 = 15 
pX2 = 470 
#both player spawning y coordinate
pY1 = 120
pY2 = 120
#score keeper
pScore1 = 0
pScore2 = 0

playerWidth = 20
playerHeight = 60

color = (0, 128, 255)

ballImg = pygame.image.load('img/ball.gif')

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q] and pY1 >= 0: pY1 -= 3
    if pressed[pygame.K_a] and pY1 <= 300 - 60: pY1 += 3
    if pressed[pygame.K_o] and pY2 >= 0: pY2 -= 3
    if pressed[pygame.K_l] and pY2 <= 300 - 60: pY2 += 3
        
    screen.fill((0, 0, 0))
        
    draw_dashed_line(screen, color, (250, 0), (250, 300), width=1, dash_length=10)
        
    pygame.draw.rect(screen, color, pygame.Rect(pX2, pY2, playerWidth, playerHeight))
    pygame.draw.rect(screen, color, pygame.Rect(pX1, pY1, playerWidth, playerHeight))
    screen.blit(ballImg, (250, 150))
    pygame.display.flip()
    clock.tick(60)
