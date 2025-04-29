import pygame

class bg:
    
    x=800
    y=450
    up_enable=True #moving background layout up
    right_enable=True #moving background layout right
    left_enable=True #moving background layout left
    down_enable=True #moving background layout down
    
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
            cls.x-=3
    @classmethod
    def left(cls):
        if cls.left_enable:
            cls.x+=3
    def blit(self,screen):
        self.bg_rect.center=(bg.x,bg.y)
        screen.blit(self.bg,self.bg_rect)
        
