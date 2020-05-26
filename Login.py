import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

screen = pygame.display.set_mode([640,480])                 #set_mode([width,hegith])
screen.fill([255,255,255])                                  #fill - 색 채우기
pygame.draw.circle(screen,THECOLORS["blue"],[320,240],30) #pygame.draw.circle(surface, color, center, radius)

pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
