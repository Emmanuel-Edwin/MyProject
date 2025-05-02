import pygame
from sys import exit
from bg_class import bg
from main_character_class import main_character
from background_image_class import background

def instruction_screen():
    global menu_colour
    #instructions
    instruction_text1=text_font.render('INSTRUCTIONS:',False,'Red')
    instruction_text2=text_font.render('Jump:Up arrow',False,'Black')
    instruction_text3=text_font.render('Move left:Left arrow',False,'Black')
    instruction_text4=text_font.render('Move right:Right arrow',False,'Black')
    instruction_text5=text_font.render('Shoot bullet:Space key',False,'Black')
    instruction_text6=text_font.render('Reload:R',False,'Black')
    instruction_text7=text_font.render('Exit:x',False,'Black')
    back_to_menu=text_font.render('<----MENU',False,'Red')
    back_to_menu_rect=back_to_menu.get_rect(center=(1400,800))
    menu_back=pygame.Surface((230,50))#back to menu button
    menu_back_rect=menu_back.get_rect(center=(1400,800))
    if menu_colour==0:
        menu_back.fill('Yellow')
    else:
        menu_back.fill('White')
    #display
    screen.fill('Light blue')
    screen.blit(instruction_text1,(500,0))
    screen.blit(instruction_text2,(500,50))
    screen.blit(instruction_text3,(500,100))
    screen.blit(instruction_text4,(500,150))
    screen.blit(instruction_text5,(500,200))
    screen.blit(instruction_text6,(500,250))
    screen.blit(instruction_text7,(500,300))
    screen.blit(menu_back,menu_back_rect)
    screen.blit(back_to_menu,back_to_menu_rect)
    # mouse sensing
    if menu_back_rect.collidepoint(pygame.mouse.get_pos()):
        menu_colour=1
        if pygame.mouse.get_pressed()[0]:
            global game_status
            game_status=0 #menu screen
    else:
        menu_colour=0
def menu():
    global game_status
    # mouse sensing
    if menu_play_rect_rect.collidepoint(pygame.mouse.get_pos()):
        menu_play_rect.fill('White')
        if pygame.mouse.get_pressed()[0]:
            game_status=1 #playing game
    else:
        menu_play_rect.fill('Yellow')
    if menu_instruction_rect_rect.collidepoint(pygame.mouse.get_pos()):
        menu_instruction_rect.fill('White')
        if pygame.mouse.get_pressed()[0]:
            game_status=2 #instruction screen
    else:
        menu_instruction_rect.fill('Yellow')
    screen.fill('Grey')
    screen.blit(menu_play_rect,play_menu_rect)
    screen.blit(play_menu,play_menu_rect)
    screen.blit(menu_instruction_rect,instruction_menu_rect)
    screen.blit(instruction_menu,instruction_menu_rect)

pygame.init()
screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN) #screen
clock=pygame.time.Clock() #clock

text_font=pygame.font.Font('C:/Windows/Fonts/Inkfree.TTF',50) #text font

play_menu=text_font.render('PLAY',False,'Blue') #text
play_menu_rect=play_menu.get_rect(center=(800,400)) #rectangle of text
menu_play_rect=pygame.Surface((135,55)) #surface
menu_play_rect.fill('Yellow') #filling colour
menu_play_rect_rect=menu_play_rect.get_rect(center=(800,400)) #rectangle of button

instruction_menu=text_font.render('INSTRUCTIONS',False,'Blue') #text
instruction_menu_rect=instruction_menu.get_rect(center=(800,500))#rectangle of text
menu_instruction_rect=pygame.Surface((395,55)) #button
menu_instruction_rect.fill('Yellow') #filling colour
menu_instruction_rect_rect=menu_instruction_rect.get_rect(center=(800,500))#rectangle of button

menu_colour=0 #colour of back to menu button--0:yellow---1:white

game_status=0 #game mode:1  menu mode:0  instruction mode:2

#jump variables
acc_gravity=.2
jump_velocity=10
jump_status=0

#main_character
main_character1=main_character()

#background_layout
bg1=bg()

#backgound_image
background1=background()

#running game
while True:

    #events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    key=pygame.key.get_pressed()
    if key[pygame.K_x]: #quiting
        pygame.quit()
        exit()
        #input events
    if game_status==1:
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

        #jump
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
    if game_status==0:
        menu()
    if game_status==2:
        instruction_screen()


    pygame.display.update()
    clock.tick(100) #clock speed
