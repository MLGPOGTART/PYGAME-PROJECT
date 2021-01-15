import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, filename, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.file = pygame.image.load(filename)
        self.image = self.file
        print("This is a Sprite loading from file", filename)
        self.w = self.image.get_rect().width
        self.h = self.image.get_rect().height
        self.x = int(x - self.w/2)
        self.y = int(y - self.h/2)
        self.v = 8
        self.y_velocity = 0
        self.is_visible = True
        self.is_left = False
        self.is_right = True
        self.is_jumping = False
        self.jumps = 10
        
    def draw(self, screen):
        if self.is_visible:
            if self.is_right:
                self.image = self.file
            if self.is_left:
                self.image = pygame.transform.flip(self.file, True, False)
            screen.blit(self.image, (self.x, self.y))
        
    def is_touching(self, other_sprite):
        if self.is_visible and other_sprite.is_visible:
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            other_sprite.rect = other_sprite.image.get_rect()
            other_sprite.rect.x = other_sprite.x
            other_sprite.rect.y = other_sprite.y
            return pygame.sprite.collide_rect(self, other_sprite)
        else: return False
        
    def hide(self):
        self.is_visible = False
    
    def show(self):
        self.is_visible = True
    
    # Thanks contributor James Johnson, class of 2020
    def change_size(self, x_percent, y_percent):
        w = self.image.get_width()
        h = self.image.get_height()
        new_w = int(w * x_percent / 100)
        new_h = int(h * y_percent / 100)
        self.image = pygame.transform.scale(self.image,(new_w,new_h))
    
    # Thanks James Johnson, class of 2020
    def clicked(self):
        if self.is_visible:
            x,y = pygame.mouse.get_pos()
            rectwidth = self.image.get_rect()[2]
            rectheight = self.image.get_rect()[3]
            
            rectxmax = int(self.x + rectwidth) #creating the furthest it can go right
            rectymax = int(self.y + rectheight) #creating the furthest it can go down
            return(  pygame.mouse.get_pressed()[0] and
                    x in range(self.x,rectxmax) and
                    y in range(self.y,rectymax) )


class Text:
    def __init__(self, surface, font, text, color, x, y):
        self.surface = surface
        self.font = font 
        self.text = text 
        self.color = color
        self.text_to_screen = self.font.render(self.text, True, self.color)
        self.is_visible = True
        
        w = self.text_to_screen.get_width()
        h = self.text_to_screen.get_height()

        self.x =  x - w/2
        self.y = y - h/2

    def hide(self):
        self.is_visible = False
    
    def show(self):
        self.is_visible = True

    def draw(self, screen):
        if self.is_visible:
            screen.blit(self.text_to_screen, (self.x, self.y))

    def clicked(self):
        x,y = pygame.mouse.get_pos()
        text_width = self.text_to_screen.get_width()
        text_height = self.text_to_screen.get_height()
        
        text_maxX = int(self.x + text_width) #creating the furthest it can go right
        text_maxY = int(self.y + text_height) #creating the furthest it can go down
        return(  pygame.mouse.get_pressed()[0] and
                 x in range(self.x,text_maxX) and
                 y in range(self.y,text_maxY) )


        