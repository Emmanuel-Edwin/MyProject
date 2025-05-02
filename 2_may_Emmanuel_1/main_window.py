import pygame
from sys import exit
from bg_class import bg
from main_character_class import main_character
from background_image_class import background

pygame.init()
screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN) #screen
clock=pygame.time.Clock() #clock
acc_gravity=.2
jump_velocity=10
jump_status=0

#main_character
main_character1=main_character()

#background_layout
bg1=bg()

#backgound_image
background1=background()

while True:

    #events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    #input events       
    key=pygame.key.get_pressed()
    if key[pygame.K_x]: #quiting
        pygame.quit()
        exit()
    bg.up_enable,bg.down_enable,bg.right_enable,bg.left_enable=main_character1.collision_main_character(bg1.bg_rect
                                                                                                        ,bg1.bg_mask
                                                                                                        ,bg.up_enable
                                                                                                        ,bg.down_enable
                                                                                                        ,bg.right_enable
                                                                                                        ,bg.left_enable)
    background.up_enable,background.down_enable,background.right_enable,background.left_enable=main_character1.collision_main_character(bg1.bg_rect
                                                                                                        ,bg1.bg_mask
                                                                                                        ,bg.up_enable
                                                                                                        ,bg.down_enable
                                                                                                        ,bg.right_enable
                                                                                                        ,bg.left_enable)
    #movement inputs
    if key[pygame.K_LEFT]:
        bg.left()
        background.left()
    if bg.down_enable==False:
        bg1.vel=0
        background1.vel=0
    if key[pygame.K_UP] and bg.down_enable==False and bg.up_enable:
        jump_status=1
        bg.y+=jump_velocity
        background.y+=jump_velocity*.5/3
        jump_velocity-=acc_gravity
    if jump_status==1:
        bg.y+=jump_velocity
        background.y+=jump_velocity*.5/3
        jump_velocity-=acc_gravity
        if jump_velocity<=0 or bg.up_enable==False:
            jump_status=0
            jump_velocity=10
            bg1.vel=-.3
            background1.vel=-.3*.5/3
    if key[pygame.K_RIGHT]:
        bg.right()
        background.right()
    if bg.down_enable and jump_status==0:
        bg1.gravity()
        background1.gravity()
      
    #screen bliting
    background1.blit(screen)
    bg1.blit(screen)
    main_character1.blit(screen)

    pygame.display.update()
    clock.tick(100) #clock speed
