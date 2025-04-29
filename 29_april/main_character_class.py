import pygame

class main_character:
    def __init__(self):
        #main_character
        self.rect_image=pygame.Surface((10,10)) #surface    ------temporary-------
        self.rect_image.fill('Red') #fill red colour    ------temporary------
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
    def collision_main_character(self,bg_rect,bg_mask,dir_up_enable,dir_down_enable,dir_right_enable,dir_left_enable):
        #bottom_collision
        if self.rect_bottom_image_mask.overlap(bg_mask,(bg_rect.x-self.rect_bottom_rect_image.x,bg_rect.y-self.rect_bottom_rect_image.y)):
            dir_down_enable=False
        else:
            dir_down_enable=True

        #top_collision
        if self.rect_top_image_mask.overlap(bg_mask,(bg_rect.x-self.rect_top_rect_image.x,bg_rect.y-self.rect_top_rect_image.y)):
            dir_up_enable=False
        else:
            dir_up_enable=True

        #right_collision
        if self.rect_right_image_mask.overlap(bg_mask,(bg_rect.x-self.rect_right_rect_image.x,bg_rect.y-self.rect_right_rect_image.y)):
            dir_left_enable=False
        else:
            dir_left_enable=True

        #left_collision
        if self.rect_left_image_mask.overlap(bg_mask,(bg_rect.x-self.rect_left_rect_image.x,bg_rect.y-self.rect_left_rect_image.y)):
            dir_right_enable=False
        else:
            dir_right_enable=True
        return dir_up_enable,dir_down_enable,dir_right_enable,dir_left_enable
    
    def blit(self,window):
        window.blit(self.rect_image,self.rect_rect_image)
