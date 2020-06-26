#---------------------------------------------#
#               메인 화면                      #
#       --------------------------            #
#       start: 2020-06-16                     #
#       --------------------------            #
#                                             #
#      게임 mainView 및 로그인 성공 시 화면     #
#      1.Game Start                           #
#      2.Help                                 #
#      3.Setting                              #
#---------------------------------------------#

#system환경 변수에 모듈을 사용하기 위해 **디렉토리**(파일 설정 x / 디렉토리까지만!!)를 설정해줘야 함
#sys.path.insert(0,new_path) -> 가장 앞에 new_path 경로 저장
import sys
# print(sys.path)
# print(sys.path[0][:-8] + 'GameRun')
sys.path.insert(0,'C:/Users/user/IndProj/Project-Game/GameRun')
sys.path.insert(0,'C:/Users/user/IndProj/Project-Game/GameRun/Help')
sys.path.insert(0,'C:/Users/user/IndProj/Project-Game/GameRun/Setting')
sys.path.insert(0,'C:/Users/user/IndProj/Project-Game/Common')
import setting,help
import run

import pygame, pygame.font
import login
import cmmlib

screen = cmmlib.screen
font = cmmlib.font

WHITE   = cmmlib.WHITE
BLACK   = cmmlib.BLACK
RED     = cmmlib.RED
GREEN   = cmmlib.GREEN
BLUE    = cmmlib.BLUE

def mainViewScreen():
    global screen

    #status 0:mainView / 1:gamestart / 2:help / 3:setting
    status = 0
    done = False

    #한번만 화면 초기화
    screen.fill(WHITE)

    gameStart_text_rect     = pygame.draw.rect(screen,BLACK,(screen.get_width() - 400,screen.get_height() - 300,200,30),1)#gamestart
    gameHelp_text_rect      = pygame.draw.rect(screen,BLACK,(screen.get_width() - 400,screen.get_height() - 250,200,30),1)#help
    gameSetting_text_rect   = pygame.draw.rect(screen,BLACK,(screen.get_width() - 400,screen.get_height() - 200,200,30),1)#setting

    gameStart_text      = "Game Start"
    gameHelp_text       = "Game Help"
    gameSetting_text    = "Game Setting"

    gameStart_text_surface      = font.render(gameStart_text,True,BLACK)
    gameHelp_text_surface       = font.render(gameHelp_text,True,BLACK)
    gameSetting_text_surface    = font.render(gameSetting_text,True,BLACK)

    screen.blit(gameStart_text_surface,     cmmlib.alignCenter(gameStart_text_surface,gameStart_text_rect))
    screen.blit(gameHelp_text_surface,      cmmlib.alignCenter(gameHelp_text_surface,gameHelp_text_rect))
    screen.blit(gameSetting_text_surface,   cmmlib.alignCenter(gameSetting_text_surface,gameSetting_text_rect))

    pygame.display.flip()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if gameStart_text_rect.collidepoint(event.pos):
                    status = 1
                    done = True

                if gameHelp_text_rect.collidepoint(event.pos):
                    status = 2
                    done = True

                if gameSetting_text_rect.collidepoint(event.pos):
                    status = 3
                    done = True
    return status

class MainView:
    def __init__(self):
        self.state  = ''
        self.id     = ''
        self.pw     = ''
        self.usr = [self.state,[self.id,self.pw]]

    def system(self):
        if self.usr[0] == '':
            usr_info = login.Login()
            if usr_info.loginScreen():
                self.usr[0] = 0
                self.usr[1] = usr_info.user_check
                print('self.usr : ',self.usr)

        #선택 받을 때까지 화면 띄우기
        while(self.usr[0] == 0):
            print('mainView')
            #usr.status 에 mainView에서 받아온 상태값을 저장
            self.usr[0] = mainViewScreen()

        if self.usr[0] == 1:
            print('game start')
            rungame = run.Run()

        if self.usr[0] == 2:
            print('game help')

        if self.usr[0] == 3:
            print('game setting')

def main():
    user = MainView()
    user.system()


if __name__=='__main__':main()
