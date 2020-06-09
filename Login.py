import pygame, pygame.font
import sys
import tmpdb
import tmpexample
from pygame.color import THECOLORS

WHITE   = (255,255,255)
BLACK   = (0,0,0)
RED     = (255,0,0)
GREEN   = (0,255,0)
BLUE    = (0,0,255)

#pygame 모듈 이니시
screen = pygame.display.set_mode([620,480])  #set_mode([width,hegith])
pygame.display.set_caption("Game Title")

#로그인 화면 기본 설정
def LoginScreen():
    #id 또는 pw 가 일치할 경우 login 성공일 떄 창 닫기
    id_success = False;
    pw_success = False;
    #프로그램 종료(pygame.quit()) 종료일 떄 창 닫기
    done = False;

    id_active  = False
    pw_active  = False
    id_text = 'ID : '
    id_input = ''
    pw_text = 'PW : '
    pw_input = ''
    clock   = pygame.time.Clock()

    action_flag = False

    #폰트 초기화
    font = pygame.font.SysFont("consolas",15,20,3)
    pygame.font.init()

    #로그인 처리
    #id와 pw가 모두 true값으로 고쳐지면 프로그램 나오기
    #혹은 done 이 true로 고쳐지면 프로그램 나오기
    while (not (id_success and pw_success)) and not done:
        screen.fill(WHITE)

        #pygame.draw.rect(surface,color,rect,width(==border))
        #rect(left,top,width,height) -> type
        #id
        id_border       = pygame.draw.rect(screen,BLACK,(screen.get_width() - 400,screen.get_height() - 200,200,20),1)
        id_text_rect    = pygame.draw.rect(screen,WHITE,(id_border[0]+1,id_border[1]+1,29,18),0)
        id_input_rect   = pygame.draw.rect(screen,WHITE,(id_text_rect[0]+45,id_text_rect[1],124,18),0)

        #pw
        pw_border       = pygame.draw.rect(screen,BLACK,(screen.get_width() - 400,screen.get_height() - 180,200,20),1)
        pw_text_rect    = pygame.draw.rect(screen,WHITE,(pw_border[0]+1,pw_border[1]+1,29,18),0)
        pw_input_rect   = pygame.draw.rect(screen,WHITE,(pw_text_rect[0]+45,pw_text_rect[1],124,18),0)


        #고정 text surface 랜더링
        id_text_surface = font.render(id_text,True,BLACK)
        pw_text_surface = font.render(pw_text,True,BLACK)

        #blit(dest,src) -> dest를 src에 붙여넣는 함수 (위에다가 덧 씌우는 형식임)
        #고정 text 값 화면에 붙여주기
        screen.blit(id_text_surface,(id_text_rect.x+5,id_text_rect.y+2.5))
        screen.blit(pw_text_surface,(pw_text_rect.x+5,pw_text_rect.y+2.5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            #마우스가 클릭이 특정부분에 눌리면 active 활성화 (이때 active는 플래그와 같은 역할 )
            if event.type == pygame.MOUSEBUTTONDOWN:
                #기본은 id , pw active 비활성화
                id_active = False
                pw_active = False
                #클릭 됐을 경우 active 활성화
                if id_input_rect.collidepoint(event.pos):
                    id_active = not id_active
                elif pw_input_rect.collidepoint(event.pos):
                    pw_active = not pw_active

            if event.type == pygame.KEYDOWN:
                if id_active:
                    if event.key == pygame.K_RETURN:
                        id_success = True
                        id_text_rect = 'ID : '
                        print(id_input)
                    elif event.key == pygame.K_BACKSPACE:
                        id_input = id_input[:-1]
                    else:
                        id_input += event.unicode
                elif pw_active:
                    if event.key == pygame.K_RETURN:
                        pw_success = True
                        pw_text_rect = 'PW : '
                        print(pw_input)
                    elif event.key == pygame.K_BACKSPACE:
                        pw_input = pw_input[:-1]
                    else:
                        pw_input += event.unicode



            # 로그인에 성공할 경우 user_info를 리턴
            if tmpdb.login_check(id_input,pw_input) == True:
                user_info = []
                user_info.append([id_input,pw_input])
                print("login success")
                return user_info
            else:
                print("login false")
                continue

        #사용자에게 받아온 입력 값 랜더링
        id_input_surface = font.render(id_input,True,BLACK)
        pw_input_surface = font.render(pw_input,True,BLACK)

        #사용자에게 받아온 입력 값 화면에 붙여주기
        screen.blit(id_input_surface,(id_input_rect.x+5,id_input_rect.y+2.5))
        screen.blit(pw_input_surface,(pw_input_rect.x+5,pw_input_rect.y+2.5))

        #display 새로고침
        pygame.display.flip()

def main():
    pygame.init()

    if LoginScreen() == True:
        tmpexample.game(screen,user_info)



if __name__ == '__main__':  main()
