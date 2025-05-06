import pygame
from sys import exit

pygame.init()
screen=pygame.display.set_mode((1366,700))
pygame.display.set_caption("Firing")
clock = pygame.time.Clock()
test_font=pygame.font.Font(None,50)

x=50
y=300

sky_surface = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (5).png").convert()
gun_surface = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (8).png").convert()
text_surface=test_font.render('Reload!!',False,'Black')
text_surface2=test_font.render('Reloading!!',False,'Black')


B1= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B2= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B3= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B4= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B5= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B6= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B7= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B8= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B9= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B10= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B11= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B12= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B13= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B14= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B15= pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()


Bullet_list=[B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,B15]
Used_list=[]

bul_stat=False
bullet_rect=Bullet_list[0].get_rect(topleft=(x,y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if len(Bullet_list)==1:
        pygame.time.delay(3000) 
        screen.blit(text_surface2,(300,800))
        Bullet_list.extend(Used_list)
        

    if len(Bullet_list)<=10:
        screen.blit(text_surface,(300,800))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        pygame.time.delay(5000) 
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

