import pygame
from sys import exit

pygame.init()
screen=pygame.display.set_mode((1366,700))
pygame.display.set_caption("Firing")
clock = pygame.time.Clock()
test_font=pygame.font.Font(None,50)

x=50
y=300

sky_surface = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (5).png").convert() #.convert_alpha() is more efficient
gun_surface = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (8).png").convert() #.convert_alpha() is more efficient
text_surface=test_font.render('Reload!!',False,'Black')
text_surface2=test_font.render('Reloading!!',False,'Black')


B1= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()#you only need B1 (B2 to B15 are unnecessary)

Bullet_list=[B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1] #This could be [B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1]
Used_list=[]

bul_stat=False
bullet_rect=Bullet_list[0].get_rect(topleft=(x,y))
Re_war=False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if len(Bullet_list)==1:
        pygame.time.delay(3000) #use a seperate timer instead of this (This causes the whole program to pause) 
        screen.blit(text_surface2,(300,800))
        Bullet_list.extend(Used_list)
        

    if len(Bullet_list)<=5:
        Re_war=True

    if len(Bullet_list)>=11:
        Re_war=False

    if Re_war==True:
        screen.blit(text_surface,(300,800))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        pygame.time.delay(5000) #use a seperate timer instead of this (This causes the whole program to pause)  
        Bullet_list.extend(Used_list)

    screen.blit(sky_surface,(0,0))
    screen.blit(gun_surface,(50,300))
    screen.blit(Bullet_list[0],bullet_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bul_stat=True

    if bul_stat==True:
        bullet_rect.right+=100

    if bullet_rect.right>=1600:
        Used_list.append(Bullet_list[0])
        Bullet_list.pop(0)
        bullet_rect=Bullet_list[0].get_rect(topleft=(x,y))
        screen.blit(Bullet_list[0],(x,y))
        bul_stat=False

    pygame.display.update()
    clock.tick(60)

