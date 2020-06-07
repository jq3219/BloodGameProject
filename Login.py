import pygame, pygame.font
import sys
from pygame.color import THECOLORS

WHITE   = (255,255,255)
BLACK   = (0,0,0)
RED     = (255,0,0)
GREEN   = (0,255,0)
BLUE    = (0,0,255)



#로그인 화면 기본 설정
def LoginScreen():
    done    = False
    id_active  = False
    pw_active  = False
    id_text = 'ID : '
    pw_text = 'PW : '
    clock   = pygame.time.Clock()

    #pygame 모듈 이니시
    screen = pygame.display.set_mode([620,480])  #set_mode([width,hegith])
    pygame.display.set_caption("Game Title")

    #폰트 초기화
    font = pygame.font.SysFont("consolas",15,20,3)
    pygame.font.init()

#로그인 처리
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #마우스가 클릭이 특정부분에 눌리면 active 활성화 (이때 active는 플래그와 같은 역할 )
            if event.type == pygame.MOUSEBUTTONDOWN:
                id_active = False
                pw_active = False
                if idRect.collidepoint(event.pos):
                    id_active = not id_active
                elif pwRect.collidepoint(event.pos):
                    pw_active = not pw_active
            if event.type == pygame.KEYDOWN:
                if id_active:
                    if event.key == pygame.K_RETURN:
                        print(id_text)
                        id_text = 'ID : '
                    elif event.key == pygame.K_BACKSPACE:
                        id_text = id_text[:-1]
                    else:
                        id_text += event.unicode
                elif pw_active:
                    if event.key == pygame.K_RETURN:
                        print(pw_text)
                        pw_text = 'PW : '
                    elif event.key == pygame.K_BACKSPACE:
                        pw_text = pw_text[:-1]
                    else:
                        pw_text += event.unicode

        screen.fill(WHITE)

        #pygame.draw.rect(surface,color,rect,width(==border))
        #rect(left,top,width,height) -> type
        #id
        idRect    = pygame.draw.rect(screen,WHITE,(screen.get_width() - 400,screen.get_height() - 200,200,20),1)
        id_border = pygame.draw.rect(screen,BLACK,(screen.get_width() - 398,screen.get_height() - 198,202,22),1)
        #pw
        pwRect    = pygame.draw.rect(screen,WHITE,(screen.get_width() - 400,screen.get_height() - 180,200,20),0)
        pw_border = pygame.draw.rect(screen,BLACK,(screen.get_width() - 398,screen.get_height() - 178,202,22),1)

        id_surface = font.render(id_text,True,BLACK)
        pw_surface = font.render(pw_text,True,BLACK)

        #blit(dest,src) -> dest를 src에 붙여넣는 함수 (위에다가 덧 씌우는 형식임)
        # screen.blit(id_border,screen)
        screen.blit(id_surface,(idRect.x+5,idRect.y+5))
        screen.blit(pw_surface,(pwRect.x+5,pwRect.y+5))

        #display 새로고침
        pygame.display.flip()

def main():
    pygame.init()
    LoginScreen()
    pygame.quit()

if __name__ == '__main__':  main()
