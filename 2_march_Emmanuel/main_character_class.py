import pygame
from bg_class import bg
from background_image_class import background

class main_character:
    def __init__(self):
        #main_character
        self.rect_image=pygame.Surface((20,20)) #surface    ------temporary-------
        self.rect_image.fill('Green') #fill red colour    ------temporary------
        self.rect_rect_image=self.rect_image.get_rect(center=(700,450)) #rectangle
        self.rect_image_mask=pygame.mask.from_surface(self.rect_image) #mask

        #character_bottom
        self.rect_bottom_image=pygame.Surface((5,1)) #surface
        self.rect_bottom_image.fill('Red') #fill red colour
        self.rect_bottom_rect_image=self.rect_bottom_image.get_rect(center=(700,455)) #rectangle
        self.rect_bottom_image_mask=pygame.mask.from_surface(self.rect_bottom_image) #mask

        #character_top
        self.rect_top_image=pygame.Surface((5,1)) #surface
        self.rect_top_image.fill('Red') #fill red colour
        self.rect_top_rect_image=self.rect_top_image.get_rect(center=(700,445)) #rectangle
        self.rect_top_image_mask=pygame.mask.from_surface(self.rect_top_image) #mask

        #character_right
        self.rect_right_image=pygame.Surface((1,5)) #surface
        self.rect_right_image.fill('Red') #fill red colour
        self.rect_right_rect_image=self.rect_right_image.get_rect(center=(695,450)) #rectangle
        self.rect_right_image_mask=pygame.mask.from_surface(self.rect_right_image) #mask

        #character_left
        self.rect_left_image=pygame.Surface((1,5)) #surface
        self.rect_left_image.fill('Red') #fill red colour
        self.rect_left_rect_image=self.rect_left_image.get_rect(center=(705,450)) #rectangle
        self.rect_left_image_mask=pygame.mask.from_surface(self.rect_left_image) #mask

        #character_sub_bottom
        self.sub_rect_bottom_image=pygame.Surface((17,1)) #surface
        self.sub_rect_bottom_image.fill('Blue') #fill red colour
        self.sub_rect_bottom_rect_image=self.rect_bottom_image.get_rect(center=(694.5,460)) #rectangle
        self.sub_rect_bottom_image_mask=pygame.mask.from_surface(self.rect_bottom_image) #mask

        #character_sub_top
        self.sub_rect_top_image=pygame.Surface((17,1)) #surface
        self.sub_rect_top_image.fill('Blue') #fill red colour
        self.sub_rect_top_rect_image=self.rect_top_image.get_rect(center=(694,440)) #rectangle
        self.sub_rect_top_image_mask=pygame.mask.from_surface(self.rect_top_image) #mask

        #character_sub_right
        self.sub_rect_right_image=pygame.Surface((1,20)) #surface
        self.sub_rect_right_image.fill('Blue') #fill red colour
        self.sub_rect_right_rect_image=self.rect_right_image.get_rect(center=(690,442)) #rectangle
        self.sub_rect_right_image_mask=pygame.mask.from_surface(self.rect_right_image) #mask

        #character_sub_left
        self.sub_rect_left_image=pygame.Surface((1,20)) #surface
        self.sub_rect_left_image.fill('Blue') #fill red colour
        self.sub_rect_left_rect_image=self.rect_left_image.get_rect(center=(710,441.5)) #rectangle
        self.sub_rect_left_image_mask=pygame.mask.from_surface(self.rect_left_image) #mask
    def collision_main_character(self,bg_rect,bg_mask,dir_up_enable,dir_down_enable,dir_right_enable,dir_left_enable):
        if self.rect_image_mask.overlap(bg_mask,(bg_rect.x-self.rect_rect_image.x-10,bg_rect.y-self.rect_rect_image.y)) and dir_up_enable==False:
            bg.y-=1
            background.y-=1*.5/3
        if self.rect_image_mask.overlap(bg_mask,(bg_rect.x-self.rect_rect_image.x-10,bg_rect.y-self.rect_rect_image.y)) and dir_down_enable==False and dir_up_enable:
            bg.y+=.2
            background.y+=.2*.5/3
        if self.rect_image_mask.overlap(bg_mask,(bg_rect.x-self.rect_rect_image.x+15,bg_rect.y-self.rect_rect_image.y)) and dir_left_enable==False:
            bg.x-=1
            background.x-=1*.5/3
        if self.rect_image_mask.overlap(bg_mask,(bg_rect.x-self.rect_rect_image.x-10,bg_rect.y-self.rect_rect_image.y)) and dir_right_enable==False and dir_up_enable:
            bg.x+=1
            background.x+=1*.5/3
        #bottom_collision
        if self.rect_bottom_image_mask.overlap(bg_mask,(bg_rect.x-self.rect_bottom_rect_image.x,bg_rect.y-self.rect_bottom_rect_image.y)):
            dir_down_enable=False
        elif self.sub_rect_bottom_image_mask.overlap(bg_mask,(bg_rect.x-self.sub_rect_bottom_rect_image.x,bg_rect.y-self.sub_rect_bottom_rect_image.y)):
            dir_down_enable=False
        else:
            dir_down_enable=True

        #top_collision
        if self.rect_top_image_mask.overlap(bg_mask,(bg_rect.x-self.rect_top_rect_image.x,bg_rect.y-self.rect_top_rect_image.y)):
            dir_up_enable=False
        elif self.sub_rect_top_image_mask.overlap(bg_mask,(bg_rect.x-self.sub_rect_top_rect_image.x,bg_rect.y-self.sub_rect_top_rect_image.y)):
            dir_up_enable=False
        else:
            dir_up_enable=True

        #right_collision
        if self.rect_right_image_mask.overlap(bg_mask,(bg_rect.x-self.rect_right_rect_image.x,bg_rect.y-self.rect_right_rect_image.y)):
            dir_left_enable=False
        elif self.sub_rect_right_image_mask.overlap(bg_mask,(bg_rect.x-self.sub_rect_right_rect_image.x,bg_rect.y-self.sub_rect_right_rect_image.y)):
            dir_left_enable=False
        else:
            dir_left_enable=True

        #left_collision
        if self.rect_left_image_mask.overlap(bg_mask,(bg_rect.x-self.rect_left_rect_image.x,bg_rect.y-self.rect_left_rect_image.y)):
            dir_right_enable=False
        elif self.sub_rect_left_image_mask.overlap(bg_mask,(bg_rect.x-self.sub_rect_left_rect_image.x,bg_rect.y-self.sub_rect_left_rect_image.y)):
            dir_right_enable=False
        else:
            dir_right_enable=True
            
        return dir_up_enable,dir_down_enable,dir_right_enable,dir_left_enable
    
    def blit(self,window):
        window.blit(self.rect_image,self.rect_rect_image)
        window.blit(self.sub_rect_top_image,self.sub_rect_top_rect_image)
        window.blit(self.sub_rect_bottom_image,self.sub_rect_bottom_rect_image)
        window.blit(self.sub_rect_right_image,self.sub_rect_right_rect_image)
        window.blit(self.sub_rect_left_image,self.sub_rect_left_rect_image)
