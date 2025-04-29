import pygame
from sys import exit
from bg_class import bg
from main_character_class import main_character

pygame.init()
screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN) #screen
clock=pygame.time.Clock() #clock

#main_character
main_character1=main_character()

#background_layout
bg1=bg()

while True:

    screen.fill('Black') #-----------temporary--------
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
    #movement inputs
    if key[pygame.K_LEFT]:
        bg.left()
    if key[pygame.K_DOWN]:
        bg.down()
    if key[pygame.K_UP]:
        bg.up()
    if key[pygame.K_RIGHT]:
        bg.right()
        
    #screen bliting    
    bg1.blit(screen)
    main_character1.blit(screen)
    bg.up_enable,bg.down_enable,bg.right_enable,bg.left_enable=main_character1.collision_main_character(bg1.bg_rect,bg1.bg_mask,bg.up_enable,bg.down_enable,bg.right_enable,bg.left_enable)
        
    pygame.display.update()
    clock.tick(100) #clock speed
