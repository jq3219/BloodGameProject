import pygame as pg
class Hero(name):
    def __init__(self,name):
        self.name = name
        self.status = ['hp','mp','speed','power']
        self.ability = ['str','dex','int','luck']
        #skill 활성화
        self.skill = ['skill1','skill2','skill3']

        #전사
        if self.name == 'hero1':
            self.status = [75,30,5,7]
            self.ability = [5,4,1,1]
            self.skill = [0,0,0]

        #궁수
        elif self.name == 'hero2':
            self.status = [60,40,7,5]
            self.ability = [3,5,1,2]
            self.skill = [0,0,0]

        #법사
        elif self.name == 'hero3':
            self.status = [35,70,5,3]
            self.ability = [1,2,5,3]
            self.skill = [0,0,0]

        #도적
        elif self.name == 'hero4':
            self.status = [40,50,10,3]
            self.ability = [1,4,1,5]
            self.skill = [0,0,0]

    #level up할 경우 stat 상승량 설정
    def level_up(self,name):
        #status[hp,mp,speed,power]
        #ability[str,dex,int,luck]
        if self.name == 'hero1':
            self.status[0] += 3
            self.status[1] += 2
            self.status[2] += 1
            self.status[3] += 2

        elif self.name == 'hero2':
            self.status[0] += 2
            self.status[1] += 2
            self.status[2] += 2
            self.status[3] += 2

        elif self.name == 'hero3':
            self.status[0] += 2
            self.status[1] += 4
            self.status[2] += 2
            self.status[3] += 1

        elif self.name == 'hero4':
            self.status[0] += 2
            self.status[1] += 2
            self.status[2] += 4
            self.status[3] += 2

    #upgrade에 따른 ability 상승량 설정
    def upgrade(self,name,abil):
        if self.name == 'hero1':
            self.ability[abil]
            pass

        elif self.name == 'hero2':
            pass

        elif self.name == 'hero3':
            pass

        elif self.name == 'hero4':
            pass

    #skill 구성 // 이 부분을 클래스로 모든 스킬 구현해서 cc 기 등을 구분할 지 아니면 그냥 하나에 다 넣을지 고민중
    def skillSet(self,name):
