import pygame
from sys import exit
from random import randint
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:/Users/emman/OneDrive/images-removebg-preview.png").convert_alpha()
        self.rect=self.image.get_rect(midbottom=(200,300))

def display_score():
    current_time=(pygame.time.get_ticks()-start_time)//1000
    score_surface=test_font.render(f'score:{current_time}',False,(64,64,64))
    score_rect=score_surface.get_rect(center=(400,50))
    screen.blit(score_surface,score_rect)
    return current_time
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x-=6
            if obstacle_rect.bottom==370:
                screen.blit(new_dino_surface,obstacle_rect)
            else:
                screen.blit(fly_surface,obstacle_rect)
        obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x>-100]
        return obstacle_list
    else:
        return []
def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True
pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
Clock=pygame.time.Clock()
game_active=False
score=0

player=player()
test_font=pygame.font.Font('C:/Windows/Fonts/ALGER.TTF',50)
game_active=True
start_time=0
ground_surface=pygame.image.load("C:/Users/emman/OneDrive/ground-removebg-preview.png").convert_alpha()
sky_surface=pygame.image.load("C:/Users/emman/OneDrive/sky.jpg").convert_alpha()
player_surface=pygame.image.load("C:/Users/emman/OneDrive/images-removebg-preview.png").convert_alpha()
player_stand=pygame.image.load("C:/Users/emman/OneDrive/images-removebg-preview.png").convert_alpha()
player_stand=pygame.transform.rotozoom(player_stand,0,0.67)
player_stand_rect=player_stand.get_rect(center=(400,200))
game_name=test_font.render('Pixel Runner',False,(111,196,169))
game_rect=game_name.get_rect(center=(400,70))
fly_surface=pygame.image.load("C:/Users/emman/OneDrive/fly_cllipart.png").convert_alpha()
fly_surface=pygame.transform.scale(fly_surface,(70,70))
game_message=test_font.render('Press space to run',False,(111,196,169))
game_mes_rect=game_message.get_rect(center=(400,340))

new_ground_surface=pygame.transform.scale(ground_surface,(800,100))
new_sky_surface=pygame.transform.scale(sky_surface,(800,400))
score_surf=test_font.render('My game',False,(64,64,64))
score_rect=score_surf.get_rect(center=(400,50))
dino_surface=pygame.image.load("C:/Users/emman/OneDrive/dinonoback.png").convert_alpha()
new_dino_surface=pygame.transform.scale(dino_surface,(70,70))
new_player_surface=pygame.transform.scale(player_surface,(70,70))
player_rect=new_player_surface.get_rect(midtop=(80,300))
#dino_rect=new_dino_surface.get_rect(midtop=(600,300))
player_gravity=-20
obstacle_rect_list=[]
obstacle_timer=pygame.USEREVENT+1
pygame.time.set_timer(obstacle_timer,1500)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom>=375:
                    player_gravity=-20
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and player_rect.bottom>=375:
                    player_gravity=-20
        else:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game_active=True
                #dino_rect.left=800
                start_time=pygame.time.get_ticks()
        if event.type==obstacle_timer and game_active:
            if randint(0,1):
                obstacle_rect_list.append(new_dino_surface.get_rect(midtop=(randint(900,1100),300)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(midtop=(randint(900,1100),210)))
    if game_active==True:    
        screen.blit(new_sky_surface,(0,0))
        screen.blit(new_ground_surface,(0,300))
        pygame.draw.rect(screen,'#c0e8ec',score_rect)
        pygame.draw.rect(screen,'#c0e8ec',score_rect,6)
        #pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos(),10)
        #pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,100))
        #screen.blit(score_surf,score_rect)
        score=display_score()
        key=pygame.key.get_pressed()
        #if key[pygame.K_SPACE]:
            #print('jump')
        player_gravity+=1
        player_rect.y+=player_gravity
        obstacle_rect_list=obstacle_movement(obstacle_rect_list)
        if player_rect.bottom>=375:
            player_rect.bottom=375
        screen.blit(new_player_surface,player_rect)
        #if dino_rect.right<=0:
            #dino_rect.left=800
        #screen.blit(new_dino_surface,dino_rect)
        #dino_rect.x-=6
        #if player_rect.colliderect(dino_rect):
            #print('collision')
        #mouse_pos=pygame.mouse.get_pos()
        #if player_rect.collidepoint(mouse_pos):
            #print(pygame.mouse.get_pressed())
        #if dino_rect.colliderect(player_rect):
            #pygame.quit()
            #exit()
            #game_active=False
        game_active=collisions(player_rect,obstacle_rect_list)
    else:
        obstacle_rect_list.clear()
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        score_message=test_font.render(f'Your score:{score}',False,(111,196,169))
        score_message_rect=score_message.get_rect(center=(400,330))
        screen.blit(game_name,game_rect)
        if score==0:
            screen.blit(game_message,game_mes_rect)
        else:
            screen.blit(score_message,score_message_rect)
    pygame.display.update()
    Clock.tick(60)
