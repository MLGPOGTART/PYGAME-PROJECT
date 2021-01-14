import pygame 
from sprite import Sprite
from sprite import Text

############################# INIT #####################################
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

clock = pygame.time.Clock()

pygame.display.init()
screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
pygame.display.set_caption("Dungeon Raider")
pygame.key.set_repeat(10)
pygame.mixer.init()
pygame.font.init()

font = pygame.font.SysFont(None, 25)
white = (255, 255, 255)
black = (0, 0, 0)


############################### MEDIA ##################################
logo = pygame.image.load('Logo.png')
title_bkgrd = pygame.image.load("Main Menu Background.jpg")
tutorial_bkrgrd = pygame.image.load('tutorial_background.jpg')
play_bkrgrd = pygame.image.load('first level.png')


player = Sprite("player.png", 640, 660)
play_button = Sprite('Play_Button.png', 415, 630)
tutorial_button = Sprite('Tutorial_Button.png', 640, 630)
quit_button = Sprite('Quit_Button.png', 865, 630)

bkgd_music = pygame.mixer.music.load('sword man.wav')
pygame.mixer.music.play(loops=-1, start=0.0)
pygame.mixer.music.set_volume(.06)

menu_click = pygame.mixer.Sound('click sound.wav')


tutorial_text = Text(screen, font, 'GAMING TIME', white, 640, 360)
pygame.display.set_icon(logo)


'''SETUP CODE'''
class Game:
    def __init__(self):
        self.run = True
        self.title = True
        self.tutorial = False
        self.play = False
    
    def title_screen(self):
        screen.blit(title_bkgrd, (0,0))
        play_button.draw(screen)
        tutorial_button.draw(screen)
        quit_button.draw(screen) 
        
        pygame.display.flip() 

        for event in pygame.event.get():        
            if event.type == pygame.QUIT:
                self.title = False 
                self.run = False
            elif play_button.clicked():
                menu_click.play(loops=0, maxtime=0)
                player.x, player.y = 1, 690 - player.h
                self.title = False
                self.play = True
                print('Play button clicked.')                
            elif tutorial_button.clicked():
                menu_click.play(loops=0, maxtime=0)
                player.x, player.y = SCREEN_WIDTH/2, SCREEN_HEIGHT - player.h
                self.title = False
                self.tutorial = True                   
                print('Tutorial button clicked.')
            elif quit_button.clicked():
                menu_click.play(loops=0, maxtime=0)
                self.title = False
                self.run = False                 

    def tutorial_screen(self):
        screen.blit(tutorial_bkrgrd, (0,0)) 
        player.draw(screen) 

        pygame.display.flip()

        movement() 
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                self.tutorial = False 
                self.run = False
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:              
                    self.tutorial = False
                    print('Escape Key Pressed.')
                    self.title = True


################ 

    def first_level(self):
        screen.blit(play_bkrgrd, (0,0))
        player.draw(screen)

        pygame.display.flip()  

        movement()
        for event in pygame.event.get():        
            if event.type == pygame.QUIT:
                self.play = False  
                self.run = False      
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print("Mouse clicked at", mouse_pos)
            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:              
                    self.play = False
                    print('Escape Key Pressed.')
                    self.title = True

######### movement controls ###############

def movement():
    if pygame.key.get_pressed()[pygame.K_a] and player.x > 0:
        player.is_right = False
        player.is_left = True
        player.x -= player.v
    if pygame.key.get_pressed()[pygame.K_d] and player.x + player.w  < SCREEN_WIDTH:
        player.is_left = False
        player.is_right = True   
        player.x += player.v    
    if not player.is_jumping:
        if pygame.key.get_pressed()[pygame.K_s] and player.y < SCREEN_HEIGHT - player.h:
            player.y += player.v
        if pygame.key.get_pressed()[pygame.K_w] and player.y > 0:
            player.is_jumping = True
    else: 
        if player.jumps >= -10:
            jump_index = 1
            if player.jumps < 0: 
                jump_index = -1
            player.y -= player.jumps**2 / 2 * jump_index
            player.jumps -= 1
        else:
            player.is_jumping = False
            player.jumps = 10

############## MAIN GAME LOOP STUFF ###########
game = Game()
while game.run:
    if game.title: 
        game.title_screen()      
    if game.play:   
        game.first_level()
    if game.tutorial:     
        game.tutorial_screen()
    clock.tick(60)       

pygame.quit() 
print("Game Ended")