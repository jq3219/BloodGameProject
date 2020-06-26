#---------------------------------------------#
#               게임 실행                      #
#       --------------------------            #
#       start: 2020-06-15                     #
#       --------------------------            #
#                                             #
#     user 정보를 기반으로 세팅                #
#     게임 룰 세팅                             #
#     게임 캐릭터 세팅                         #
#---------------------------------------------#

import sys
sys.path.insert(0,'C:/Users/user/IndProj/Project-Game/MainView')
sys.path.insert(0,'C:/Users/user/IndProj/Project-Game/Common')
import pygame, pygame.font
import random
import hero, unit, base
import cmmlib

screen  = cmmlib.screen
font    = cmmlib.font2

#현재 시각을 저장
start_time = pygame.time.get_ticks()

WHITE   = cmmlib.WHITE
BLACK   = cmmlib.BLACK
RED     = cmmlib.RED
GREEN   = cmmlib.GREEN
BLUE    = cmmlib.BLUE

TEAM = ['Blue','Red']

class Run:
    def __init__(self):
        print("Game Init")
        global screen
        #player의 인원수는 list append를 통해서 조작 / #player1 과 player2는 고정
        self.player = ['player1','player2']
        self.player_rect = []
        #plyaer의 인원수
        self.cntPlayer = 2


        self.ready_room()
        #일단 사용자1,2를 받고 나를 사용자1 로 지정(일단 팀=blue로 고정)
        # player1 = base.Base(screen,'Blue')
        # player2 = base.Base(screen,'Red')
        #
        # self.player.append(player1)
        # self.player.append(player2)

    #플레이어 추가
    def addPlayer(self):
        #add는 text가 cntplayer의 영향을 받으므로 일단 하나 올리고 시작
        #4명이 초과 될 경우 return하기전에 cntplayer를 하나 올리면서 시작했으므로 다시 하나 줄여야 함
        self.cntPlayer+=1
        if self.cntPlayer > 4:
            self.cntPlayer-=1
            #지금은 콘솔에 띄우지만 나중에 알림창으로 띄울 것
            print("Can't create more 4player")
            return

        #cntPlayer는 인원수
        self.player.append('player'+str(self.cntPlayer))


        #add 순서에 따른 위치 / player 인덱스 접근을 위해 -3(헷갈리지 않기) / 홀수(아군)은 왼쪽 / 짝수(적군)은 오른쪽
        player_rect = pygame.draw.rect(screen,BLACK,(self.player_rect[self.cntPlayer-3][0],self.player_rect[self.cntPlayer-3][1] + 30,75,15),1)
        player_text = "player"+str(self.cntPlayer)
        player_text_surface = font.render(player_text,True,BLACK)
        screen.blit(player_text_surface,cmmlib.alignCenter(player_text_surface,player_rect))

        self.player_rect.append(player_rect)

        #######################요소 확인############################
        print('self.player : ',self.player)
        print('self.player_rect : ',self.player_rect)
    #플레이어 삭제
    def delPlayer(self):
        #del는 모든 행동을 다 한 후 최종 cnt--
        if self.cntPlayer < 3:
            print("Can't delete more 2player")
            return

        #player리스트에서 카운트에 해당하는 플레이어 삭제
        self.player.remove('player'+str(self.cntPlayer))

        #해당 rect부분 흰 화면으로 덮어 씌우기
        player_rect = pygame.draw.rect(screen,WHITE,(self.player_rect[self.cntPlayer-3][0],self.player_rect[self.cntPlayer-3][1] + 30,75,15))

        #player_rect 에서 pop (임시로 del를 할 경우 위에서부터 없애는거로 처리)
        self.player_rect.pop()

        #######################요소 확인############################
        print('self.player : ',self.player)
        print('self.player_rect : ',self.player_rect)
        self.cntPlayer-=1

    #대기방 설정(인원수 조정이 가능한 대기방 설정 / 롤 봇전 처럼 구현)
    def ready_room_setting(self):
        #화면 초기화
        screen.fill(WHITE)

        #플레이어 추가 버튼
        self.add_btn_rect = pygame.draw.rect(screen,BLACK,(400,210,100,15),1)
        add_btn_text = "Add Player"
        add_btn_text_surface = font.render(add_btn_text,True,BLACK)
        screen.blit(add_btn_text_surface,cmmlib.alignCenter(add_btn_text_surface,self.add_btn_rect))

        #플레이어 삭제 버튼
        self.del_btn_rect = pygame.draw.rect(screen,BLACK,(400,240,100,15),1)
        del_btn_text = "Del Player"
        del_btn_text_surface = font.render(del_btn_text,True,BLACK)
        screen.blit(del_btn_text_surface,cmmlib.alignCenter(del_btn_text_surface,self.del_btn_rect))

        #게임 시작 버튼
        self.start_btn_rect = pygame.draw.rect(screen,BLACK,(400,300,100,15),1)
        start_btn_text = "Start"
        start_btn_text_surface = font.render(start_btn_text,True,BLACK)
        screen.blit(start_btn_text_surface,cmmlib.alignCenter(start_btn_text_surface,self.start_btn_rect))


        #플레이어1과 2는 고정
        player1_rect = pygame.draw.rect(screen,BLACK,(screen.get_width() / 6,screen.get_height() / 5,75,15),1)
        player1_text = "player1"
        player1_text_surface = font.render(player1_text,True,BLACK)
        screen.blit(player1_text_surface,cmmlib.alignCenter(player1_text_surface,player1_rect))

        player2_rect = pygame.draw.rect(screen,BLACK,(screen.get_width() / 3,screen.get_height() / 5,75,15),1)
        player2_text = "player2"
        player2_text_surface = font.render(player2_text,True,BLACK)
        screen.blit(player2_text_surface,cmmlib.alignCenter(player2_text_surface,player2_rect))

        self.player_rect.append(player1_rect)
        self.player_rect.append(player2_rect)


    def ready_room(self):
        self.ready_room_setting()
        num = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()

                if event.type==pygame.MOUSEBUTTONDOWN:
                    if self.add_btn_rect.collidepoint(event.pos):
                        self.addPlayer()
                    elif self.del_btn_rect.collidepoint(event.pos):
                        self.delPlayer()
                    elif self.start_btn_rect.collidepoint(event.pos):
                        self.game_start()
                    pass

            pygame.display.update()

    def game_start(self):
        global screen, TEAM
        running = True

        screen.fill(WHITE)

        #플레이어 베이스 생성 및 베이스 위치 리스트 요소 삭제(중복 방지)
        for player in self.player:
            #팀 요소('Blue','Red'중 하나를 임시로 선택->리스트로 반환하므로 0번째 요소 선택)
            #아직은 blue, blue가 나올수도 있고 blue red가 나올수도 있음(팀 랜덤)
            player = base.Base(random.sample(TEAM,1)[0])           #베이스 파일에서 선택할 수 있는 기본 위치 요소 중 이전에 해당되는 요소를 삭제(중복방지)
            base.org_pos.remove(player.base_info[2][0])

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    pass


            pygame.display.update()

if __name__ == '__main__':
    run = Run()
