import pygame
import sys
import tmpdb
from pygame.color import THECOLORS


pygame.init()

#pygame 모듈 이니시
screen = pygame.display.set_mode([620,480])  #set_mode([width,hegith])
pygame.display.set_caption("Game Title")

font = pygame.font.SysFont("consolas",15,20,3)
pygame.font.init()
play = True

WHITE   = (255,255,255)
BLACK   = (0,0,0)
RED     = (255,0,0)
GREEN   = (0,255,0)
BLUE    = (0,0,255)

class login:
    def __init__(self):
        #id 또는 pw 가 일치할 경우 login 성공일 떄 창 닫기
        self.id_success = False;
        self.pw_success = False;
        #프로그램 종료(pygame.quit()) 종료일 떄 창 닫기
        self.done = False;

        self.mouse_rect = pygame.Rect(0,0,10,10)
        self.id_rect    = pygame.Rect(290,280,160,23)
        self.pw_rect    = pygame.Rect(290,280,160,23)
        self.login_rect = pygame.Rect(455,280,50,50)
        self.quit_rect  = pygame.Rect(435,355,69,30)
        self.click = [1,1,0]
        self.id = 0
        self.pw = 0
        self.data = []

    def login_system(self):
        screen.fill(WHITE)
        self.mouse_rect.topleft = pygame.mouse.get_pos()

        for event in pygame.event.get():
            global play
            if event.type == pygame.MOUSEBUTTONDOWN:
                if login.mouse_rect.collidepoint(login.id_rect):
                    self.click[0] = 0
                    self.id = input()
                elif login.mouse_rect.collidepoint(login.pw_rect):
                    self.click[1] = 0
                    self.pw = input()
                elif login.mouse_rect.collidepoint(login.login_rect):
                    if self.click[2]:
                        if tmpdb.login_check(self.id,self.pw):
                            self.data.append([self.id,self.pw])
                        else:
                            print("login failed")
                elif login.mouse_rect.collidepoint(login.quit_rect):
                    play = False
            elif event.type == pygame.QUIT:
                play = False


def main():
    lg = login()
    lg.login_system()

if __name__ == '__main__':main()
