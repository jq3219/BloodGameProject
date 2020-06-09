import pygame
import Login

class game:
    def __init__(self,screen,user_info):
        user_id = user_info[0]
        user_pw = user_info[1]

        print('user_id : {} / user_pw : {}'.format(user_id,user_pw))
