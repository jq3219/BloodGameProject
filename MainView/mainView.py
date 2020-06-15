#---------------------------------------------#
#               메인 화면                      #
#       --------------------------            #
#       start: 2020-05-26                     #
#       --------------------------            #
#                                             #
#      게임 시작 파일 및 로그인 성공 시 화면     #
#      1.Game Start                           #
#      2.Help                                 #
#      3.Setting                              #
#---------------------------------------------#
import pygame,pygame.font
import login
screen = login.screen
font = login.font

WHITE   = (255,255,255)
BLACK   = (0,0,0)
RED     = (255,0,0)
GREEN   = (0,255,0)
BLUE    = (0,0,255)

#위치와 크기를 받아와서 그 중앙값 리턴
def AlignCenter(text_surface,rect):
    res = []
    res.append((rect[0] + rect[2]/2) - text_surface.get_width()/2)
    res.append((rect[1] + rect[3]/2) - text_surface.get_height()/2)

    return  res

def MainView():
    global screen

    #status 0:mainView / 1:gamestart / 2:help / 3:setting
    status = 0
    done = False

    #한번만 화면 초기화
    screen.fill(WHITE)
    gameStart_text_rect = pygame.draw.rect(screen,BLACK,(screen.get_width() - 400,screen.get_height() - 300,200,30),1)#gamestart
    gameStart_text = "Game Start"
    gameStart_text_surface = font.render(gameStart_text,True,BLACK)
    screen.blit(gameStart_text_surface,AlignCenter(gameStart_text_surface,gameStart_text_rect))

    gameHelp_text_rect = pygame.draw.rect(screen,BLACK,(screen.get_width() - 400,screen.get_height() - 250,200,30),1)#help
    gameHelp_text = "Game Help"
    gameHelp_text_surface = font.render(gameHelp_text,True,BLACK)
    screen.blit(gameHelp_text_surface,AlignCenter(gameHelp_text_surface,gameHelp_text_rect))

    gameSetting_text_rect = pygame.draw.rect(screen,BLACK,(screen.get_width() - 400,screen.get_height() - 200,200,30),1)#setting
    gameSetting_text = "Game Setting"
    gameSetting_text_surface = font.render(gameSetting_text,True,BLACK)
    screen.blit(gameSetting_text_surface,AlignCenter(gameSetting_text_surface,gameSetting_text_rect))

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

class game:
    def __init__(self):
        self.state  = ''
        self.id     = ''
        self.pw     = ''
        self.usr = [self.state,[self.id,self.pw]]

    def system(self):
        if self.usr[0] == '':
            usr_info = login.Login()
            if usr_info.LoginScreen():
                self.usr[0] = 0
                self.usr[1] = usr_info.user_check
                print('self.usr : ',self.usr)

        #선택 받을 때까지 화면 띄우기
        while(self.usr[0] == 0):
            print('mainView')
            #usr.status 에 mainView에서 받아온 상태값을 저장
            self.usr[0] = MainView()
            pass

        if self.usr[0] == 1:
            print('game start')
            pass

        if self.usr[0] == 2:
            print('game help')
            pass

        if self.usr[0] == 3:
            print('game setting')
            pass

def main():
    user = game()
    user.system()


if __name__=='__main__':main()
