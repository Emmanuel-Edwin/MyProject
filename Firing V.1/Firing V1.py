import pygame
from sys import exit
import time

pygame.init()
screen=pygame.display.set_mode((1366,700))
pygame.display.set_caption("Firing")
clock = pygame.time.Clock()
test_font=pygame.font.Font(None,50)

x=50
y=300

m=600
n=50

health=100

sky_surface = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (5).png").convert_alpha()
gun_surface = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (8).png").convert_alpha() 
player_surface = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (8).png").convert_alpha() 
text_surface=test_font.render('Reload!!',False,'Black')
text_surface2=test_font.render('Reloading!!',False,'Black')
text_surface3=test_font.render(f"Health: {health}",False,'Black')
B1= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert_alpha()

Gun_List=[]
Bullet_list=[B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1]
Used_list=[]

bul_stat=False
bullet_rect=Bullet_list[0].get_rect(topleft=(x,y))
player_rect=player_surface.get_rect(topleft=(m,n))
t1_rect=text_surface.get_rect(topleft=(1250,5))
t2_rect=text_surface2.get_rect(topleft=(1250,5))
t3_rect=text_surface3.get_rect(topleft=(5,5))

Re_war=False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(text_surface3,t3_rect)

    if len(Bullet_list)==1:
        screen.blit(text_surface2,t2_rect)
        time.sleep(3)#use a seperate timer instead of this (This causes the whole program to pause) 
        Bullet_list.extend(Used_list)

    if len(Bullet_list)<=5:
        Re_war=True

    if len(Bullet_list)>=11:
        Re_war=False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        pygame.time.delay(5000) #use a seperate timer instead of this (This causes the whole program to pause)  
        Bullet_list.extend(Used_list)

    screen.blit(sky_surface,(0,0))
    screen.blit(gun_surface,(50,300))
    screen.blit(Bullet_list[0],bullet_rect)
    screen.blit(player_surface,player_rect)

    if Re_war==True:
        screen.blit(text_surface,(300,800))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bul_stat=True
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.top-=5

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        player_rect.bottom+=5

    if bul_stat==True:
        bullet_rect.right+=100

    if player_rect.colliderect(bullet_rect):
        Bullet_list.pop(0)
        screen.blit(Bullet_list[0],bullet_rect)
        health-=1
        print("Collision detected between rect1 and rect2!",health)

    if bullet_rect.right>=1600:
        Used_list.append(Bullet_list[0])
        Bullet_list.pop(0)
        bullet_rect=Bullet_list[0].get_rect(topleft=(x,y))
        screen.blit(Bullet_list[0],(x,y))
        bul_stat=False

    
    pygame.display.update()
    clock.tick(60)

