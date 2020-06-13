import Login
# from gameRun import game
# import pygame

class game:
    def __init__(self):
        self.state  = ''
        self.id     = ''
        self.pw     = ''
        self.usr = [self.state,[self.id,self.pw]]

    def system(self):
        if self.usr[0] == '':
            usr_info = Login.Login()
            if usr_info.LoginScreen():
                self.usr[0] = 1
                self.usr[1] = usr_info.user_check
                print('self.usr : ',self.usr)

        # elif self.state == 1:
        #     gameRun.game()




def main():
    start = game()
    start.system()


if __name__=='__main__':main()
