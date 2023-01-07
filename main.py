import pygame,sys

screen_width = 800
screen_hight = 600
screen_size = screen_width,screen_hight

menu_bg = pygame.image.load("menu_bg.jpg")
menu_bg = pygame.transform.scale(menu_bg, (screen_size[0], screen_size[1]))
play_img = pygame.image.load("play.jpg")
play_img = pygame.transform.scale(play_img, (screen_size[0]/3.2, screen_size[1]/12))
score_img = pygame.image.load("score.jpg")
score_img = pygame.transform.scale(score_img, (screen_size[0]/3.2, screen_size[1]/12))
instruction_img = pygame.image.load("instruction.jpg")
instruction_img = pygame.transform.scale(instruction_img, (screen_size[0]/3.2, screen_size[1]/12))
exit_img = pygame.image.load("exit.jpg")
exit_img = pygame.transform.scale(exit_img, (screen_size[0]/3.2, screen_size[1]/12))

class Menu():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
        self.clock = pygame.time.Clock()

        self.bg = menu_bg
        self.bg_rect = self.bg.get_rect()

        self.play_img= play_img
        self.play_rect = self.play_img.get_rect()
        self.play_rect.center = screen_size[0]/2,screen_size[1]/4

        self.score_img= score_img
        self.score_rect = self.score_img.get_rect()
        self.score_rect.center = screen_size[0]/2,self.play_rect.center[1]+self.score_img.get_height()+self.score_img.get_height()/2

        self.instruction_img= instruction_img
        self.instruction_rect = self.instruction_img.get_rect()
        self.instruction_rect.center = screen_size[0]/2,self.score_rect.center[1]+self.score_img.get_height()+self.score_img.get_height()/2

        self.exit_img= exit_img
        self.exit_rect = self.exit_img.get_rect()
        self.exit_rect.center = screen_size[0]/2,self.instruction_rect.center[1]+self.score_img.get_height()+self.score_img.get_height()/2

        self.menu_button = 0


    def control(self):
        if self.play_rect.collidepoint(pygame.mouse.get_pos()):
            self.menu_button = 1
        if self.score_rect.collidepoint(pygame.mouse.get_pos()):
            self.menu_button = 2
        if self.instruction_rect.collidepoint(pygame.mouse.get_pos()):
            self.menu_button = 3
        if self.exit_rect.collidepoint(pygame.mouse.get_pos()):
            self.menu_button = 4





    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.control()

            print(self.menu_button)
            self.clock.tick(40)

            self.screen.blit(menu_bg,(0,0))
            self.screen.blit(play_img,self.play_rect)
            self.screen.blit(score_img,self.score_rect)
            self.screen.blit(instruction_img,self.instruction_rect)
            self.screen.blit(exit_img,self.exit_rect)
            pygame.display.flip()



Menu().run()
