import pygame
from sys import exit

pygame.init()
screen=pygame.display.set_mode((1366,700))
pygame.display.set_caption("Firing")
clock = pygame.time.Clock()

sky_surface = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (5).png").convert()
gun_surface = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (8).png").convert()
B1 = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B2 = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B3 = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B4 = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B5 = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B6 = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B7 = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B8 = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B9 = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()
B10 = pygame.image.load("D:\\VS Code\\Blah Blah\\Untitled design (7).png").convert()

L_New=[B1,B2,B3,B4,B5,B6,B7,B8,B9,B10]
L_Used=[]

bullet_rect=L_New[0].get_rect(bottomright=(70,250))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface,(0,0))
    screen.blit(gun_surface,(50,300))
    if L_New:
        screen.blit(L_New[0],(50,300))

    Bul_stat=0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]: 
        Bul_stat+=1

    if Bul_stat==1:
        bullet_rect.right+=400

    if bullet_rect.left<=1366:
        L_Used.append(L_New[0])
        L_New.pop(0)
        Bul_stat-=1
    
    pygame.display.update()
    clock.tick(60)