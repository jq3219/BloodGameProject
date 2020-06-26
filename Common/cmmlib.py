import pygame, pygame.font
import sys
WHITE   = (255,255,255)
BLACK   = (0,0,0)
RED     = (255,0,0)
GREEN   = (0,255,0)
BLUE    = (0,0,255)

screen = pygame.display.set_mode([620,480])  #set_mode([width,hegith])
pygame.display.set_caption("Game Title")

font = pygame.font.init()
font = pygame.font.SysFont("consolas",15,20,3)
font2 = pygame.font.SysFont("consolas",12,7,2)

#위치와 크기를 받아와서 그 중앙값 리턴 (src, dest)
def alignCenter(text_surface,rect):
    #result
    res = []
    res.append((rect[0] + rect[2]/2) - text_surface.get_width()/2)
    res.append((rect[1] + rect[3]/2) - text_surface.get_height()/2)

    return  res
# li = ['asd','fd','jj']
# li.remove('asd')
# print(li)
