#---------------------------------------------#
#               Base  Class                   #
#       --------------------------            #
#       start: 2020-06-26                     #
#       --------------------------            #
#                                             #
#       Base(진영) class                       #
#---------------------------------------------#
import sys
sys.path.insert(0,'C:/Users/user/IndProj/Project-Game/Common')
import cmmlib
import pygame
import random
#run 모듈의 screen을 global로 쓰고 싶지만 run에서 base import 하고 base에서 run import 하면 충돌일어나는 듯
#screen은 초기화에서 매개변수로 받아오기

screen = cmmlib.screen

#org_pos을 전역변수로 사용하기 위해 임시로 베이스 이미지 하나 꺼내서 사이즈 설정해줌
base_img = pygame.image.load('C:/Users/user/IndProj/Project-Game/Img/base1.PNG')
base_size = pygame.transform.scale(base_img,(int(screen.get_width()/15),int(screen.get_height()/12)))

#기본 위치 -----> 11시 / 1시 / 5시 / 7시 (각 모퉁이)
org_x_pos = [0,screen.get_width() - base_size.get_width()]
org_y_pos = [0,screen.get_height() - base_size.get_height()]

#기본 위치에서 랜덤으로 x좌표 y좌표 하나씩 얻어온 것을 pos으로 지정 (진영 위치 랜덤 생성)
org_pos = [
    [org_x_pos[0],org_y_pos[0]],
    [org_x_pos[0],org_y_pos[1]],
    [org_x_pos[1],org_y_pos[0]],
    [org_x_pos[1],org_y_pos[1]]
]

#base는 HP와 고유의 랜덤 위치
#base에 들어가야될 정보
#너비 높이 / 팀 / 위치
class Base:
    def __init__(self,team):
        global screen
        #기본 베이스
        self.base_info = ['team','hp','pos']

        #진영에 따른 베이스 이미지 로드
        if team == 'Blue':
            blue_base = pygame.image.load('C:/Users/user/IndProj/Project-Game/Img/base1.PNG')
            #blue진영 이미지 resize (임시로 screen의 가로 15분의 1 / 세로 10분의 1크기)
            base_size = pygame.transform.scale(blue_base,(int(screen.get_width()/15),int(screen.get_height()/12)))
        elif team == 'Red':
            red_base = pygame.image.load('C:/Users/user/IndProj/Project-Game/Img/base2.PNG')
            #red진영 이미지 resize (임시로 screen의 가로 15분의 1 / 세로 10분의 1크기)
            base_size = pygame.transform.scale(red_base,(int(screen.get_width()/15),int(screen.get_height()/12)))


        global org_pos
        cur_pos = random.sample(org_pos,1)
        print('org_pos : ',org_pos)
        print('cur_pos : ',cur_pos)

        self.base_info[0] = team
        self.base_info[1] = 500
        self.base_info[2] = cur_pos

        #self.base_info[3]=size(type : surface) / self.base_info[2]=랜덤 위치(type : surface)에 삽입
        screen.blit(base_size, self.base_info[2][0])

def main():
    pygame.init()

    running = True

    base = Base(screen,'Blue')
    enemy_base =Base(screen,'Red')

    pygame.display.update()

    while running:
        for event in pygame.event.type():
            if event.MOUSEBUTTONDOWN:
                if event.quit:
                    running = False
                    pygame.quit()


if __name__ =='__main__':
    main()
