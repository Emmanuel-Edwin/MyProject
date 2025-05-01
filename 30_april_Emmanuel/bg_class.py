import pygame

class bg:
    
    x=800
    y=450
    up_enable=True #moving background layout up
    right_enable=True #moving background layout right
    left_enable=True #moving background layout left
    down_enable=True #moving background layout down
    vel=0 #gravity velocity
    grav_acc=.2 #acceleration due to gravity
    
    def __init__(self):
        self.bg=pygame.image.load("C:/Users/emman/OneDrive/comp_proj/map_layout.png").convert_alpha() #import image
        self.bg=pygame.transform.rotozoom(self.bg,0,2) #transform size
        self.bg_rect=self.bg.get_rect(center=(bg.x,bg.y)) #rectangle
        self.bg_mask=pygame.mask.from_surface(self.bg) #mask
        
    @classmethod
    def up(cls):
        if cls.up_enable:
            cls.y+=3
    @classmethod
    def down(cls):
        if cls.down_enable:
            cls.y-=3
    @classmethod
    def right(cls):
        if cls.right_enable:
            cls.x-=5
    @classmethod
    def left(cls):
        if cls.left_enable:
            cls.x+=5
    
    def gravity(self):
        if bg.down_enable:
            bg.y-=self.vel
            self.vel+=self.grav_acc

    def blit(self,screen):
        self.bg_rect.center=(bg.x,bg.y)
        screen.blit(self.bg,self.bg_rect)
        
