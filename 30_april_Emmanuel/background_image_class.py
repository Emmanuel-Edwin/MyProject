import pygame

class background:
    
    x=800
    y=450
    up_enable=True #moving background layout up
    right_enable=True #moving background layout right
    left_enable=True #moving background layout left
    down_enable=True #moving background layout down
    vel=0*.5/3 #gravity velocity
    grav_acc=.2*.5/3 #acceleration due to gravity
    
    def __init__(self):
        self.image=pygame.image.load("C:/Users/emman/OneDrive/comp_proj/background.png").convert_alpha() #import image
        self.image=pygame.transform.rotozoom(self.image,0,2) #transform size
        self.rect=self.image.get_rect(center=(background.x,background.y)) #rectangle
        
    @classmethod
    def up(cls):
        if cls.up_enable:
            cls.y+=.5
    @classmethod
    def down(cls):
        if cls.down_enable:
            cls.y-=.5
    @classmethod
    def right(cls):
        if cls.right_enable:
            cls.x-=5*.5/3
    @classmethod
    def left(cls):
        if cls.left_enable:
            cls.x+=5*.5/3
    
    def gravity(self):
        if background.down_enable:
            background.y-=self.vel
            self.vel+=self.grav_acc

    def blit(self,window):
        self.rect.center=(background.x,background.y)
        window.blit(self.image,self.rect)
        
