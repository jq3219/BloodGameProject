
import pygame, pygame.font
import sys
import tmpdb
# import tmpexample
from pygame.color import THECOLORS

WHITE   = (255,255,255)
BLACK   = (0,0,0)
RED     = (255,0,0)
GREEN   = (0,255,0)
BLUE    = (0,0,255)

pygame.init()
#pygame 모듈 이니시
screen = pygame.display.set_mode([620,480])  #set_mode([width,hegith])
pygame.display.set_caption("Game Title")

#폰트 초기화
font = pygame.font.SysFont("consolas",15,20,3)
pygame.font.init()

class Login:
    def __init__(self):
        #id 또는 pw 가 일치할 경우 login 성공일 떄 창 닫기
        self.id_success = False;
        self.pw_success = False;
        #프로그램 종료(pygame.quit()) 종료일 떄 창 닫기
        self.done = False;

        #rect활성화 변수
        self.id_active  = False
        self.pw_active  = False

        #입력값 받는 변수
        self.id_input = ''
        self.pw_input = ''

        #user id,pw 입력 받을 시1로 변경 -> user 정보 입력 체크
        self.user_check = [0,0]
        self.clock      = pygame.time.Clock()

    def Login_Setting(self):
        global screen
        screen.fill(WHITE)
        #pygame.draw.rect(surface,color,rect,width(==border))
        #rect(left,top,width,height) -> type

        #id
        id_border           = pygame.draw.rect(screen,BLACK,(screen.get_width() - 400,screen.get_height() - 200,200,20),1)
        id_text_rect        = pygame.draw.rect(screen,WHITE,(id_border[0]+1,id_border[1]+1,29,18),0)
        self.id_input_rect  = pygame.draw.rect(screen,WHITE,(id_text_rect[0]+45,id_text_rect[1],124,18),0)
        #pw
        pw_border           = pygame.draw.rect(screen,BLACK,(screen.get_width() - 400,screen.get_height() - 180,200,20),1)
        pw_text_rect        = pygame.draw.rect(screen,WHITE,(pw_border[0]+1,pw_border[1]+1,29,18),0)
        self.pw_input_rect  = pygame.draw.rect(screen,WHITE,(pw_text_rect[0]+45,pw_text_rect[1],124,18),0)

        id_text = 'ID : '
        pw_text = 'PW : '

        #고정 text surface 랜더링
        id_text_surface = font.render(id_text,True,BLACK)
        pw_text_surface = font.render(pw_text,True,BLACK)

        #blit(dest,src) -> dest를 src에 붙여넣는 함수 (위에다가 덧 씌우는 형식임)
        #고정 text 값 화면에 붙여주기
        screen.blit(id_text_surface,(id_text_rect.x+5,id_text_rect.y+2.5))
        screen.blit(pw_text_surface,(pw_text_rect.x+5,pw_text_rect.y+2.5))


        #-----------------------------------------------------------------#
        #회원가입
        sign_up_border      = pygame.draw.rect(screen,BLACK,(screen.get_width() - 275,screen.get_height() - 155,75,20),1)
        self.sign_up_rect   = pygame.draw.rect(screen,WHITE,(sign_up_border[0]+1,sign_up_border[1]+1,73,18))
        sign_up_text        = "Sign Up"
        sign_up_surface     = font.render(sign_up_text,True,BLACK)
        screen.blit(sign_up_surface,(self.sign_up_rect.x+2.5,self.sign_up_rect.y+2.5))


    #로그인 화면 기본 설정
    def LoginScreen(self):
        #로그인 처리
        #id와 pw가 모두 true값으로 고쳐지면 프로그램 나오기
        #혹은 done 이 true로 고쳐지면 프로그램 나오기
        while (not (self.id_success and self.pw_success)) and not self.done:
            self.Login_Setting()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                #마우스가 클릭이 특정부분에 눌리면 active 활성화 (이때 active는 플래그와 같은 역할 )
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #기본은 id , pw active 비활성화
                    self.id_active = False
                    self.pw_active = False
                    #클릭 됐을 경우 active 활성화
                    if self.id_input_rect.collidepoint(event.pos):
                        self.id_active = not self.id_active
                    elif self.pw_input_rect.collidepoint(event.pos):
                        self.pw_active = not self.pw_active
                    elif self.sign_up_rect.collidepoint(event.pos):
                        sys_id = int(tmpdb.select_max_id_num()) + 1
                        tmpdb.sign_up(sys_id,self.id_input.strip(),self.pw_input.strip())

                if event.type == pygame.KEYDOWN:
                    if self.id_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.id_input = self.id_input[:-1]
                        else:
                            self.id_input += event.unicode
                    elif self.pw_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.pw_input = self.pw_input[:-1]
                        else:
                            self.pw_input += event.unicode

                    if event.key == pygame.K_RETURN:
                        #strip 문자 공백 제거 함수 (안써주면 db들어갈 때 2번 째 인자에서 오류 생김)
                        self.user_check[0] = self.id_input.strip()
                        self.user_check[1] = self.pw_input.strip()

                        print("id : ",self.user_check[0])
                        print("pw : ",self.user_check[1])

                # 로그인에 성공할 경우 user_info를 리턴
                if not self.user_check[0]==0 and not self.user_check[1]==0:
                    if tmpdb.login_check(self.user_check[0],self.user_check[1]) == True:
                        print("login success")
                        return self.user_check
                    else:
                        self.user_check[0] = 0
                        self.user_check[1] = 0
                        print("login false")
                        continue

            #사용자에게 받아온 입력 값 랜더링
            id_input_surface = font.render(self.id_input,True,BLACK)
            pw_input_surface = font.render(self.pw_input,True,BLACK)

            #사용자에게 받아온 입력 값 화면에 붙여주기
            screen.blit(id_input_surface,(self.id_input_rect.x+5,self.id_input_rect.y+2.5))
            screen.blit(pw_input_surface,(self.pw_input_rect.x+5,self.pw_input_rect.y+2.5))

            #display 새로고침
            pygame.display.flip()

def main():
    lg = Login()
    lg.LoginScreen()
    # if LoginScreen() == True:
        # tmpexample.game(screen,user_info)

if __name__ == '__main__':  main()
