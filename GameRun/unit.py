#---------------------------------------------#
#               유닛 Class                    #
#       --------------------------            #
#       start: 2020-06-15                     #
#       --------------------------            #
#                                             #
#     기본 유닛 class                          #
#---------------------------------------------#

import pygame

#타이머 조작
clock = pygame.time.Clock()

class Unit:
    def __init__(self,screen):
        #self.status = ['team'.'hp','mp','speed','power']
        self.status = ['Blue',10,0,2,2]

        unit = pygame.image.load('C:/Users/user/IndProj/Project-Game/Img/unit.png')
        unit_size = unit.get_rect.size()
        unit_width = unit_size[0]
        unit_height = unit_size[1]

        unit_x_pos = screen_width / 2 - unit_width / 2
        unit_y_pos = screen_height / 2 - unit_height / 2
