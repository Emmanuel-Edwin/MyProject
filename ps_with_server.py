
import pygame
from sys import exit
from tkinter import*
from tkinter import messagebox
import mysql.connector as mc
import socket
import ast
import math

tick=100
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind(('192.168.0.142', 5555))

s.listen(4)
print('Waiting for connections')

conn, addr = s.accept()
print('Got connection from', addr)

co=mc.connect(host='localhost',passwd='mysql',database='pixel_shooter',user='root')
cuo=co.cursor()

window1=Tk()
window1.geometry("300x100")
window1.title("login or signin")
window1.config(background='White')
login=False 

px2=200
py2=200

a,b=800,450

def log():
    global window1
    signin_button.config(state=DISABLED)
    login_button.config(state=DISABLED)
    window=Tk()
    window.geometry("300x300")
    window.title("login")
    window.config(background='White')
    def login():
        global login
        global passwd,use
        passwd=pas.get()
        use=user.get()
        pas.delete(0,END)
        user.delete(0,END)
        if passwd.isdigit():
            q="Select password,username from udet where password={} and username='{}'".format(passwd,use)
            cuo.execute(q)
            d=cuo.fetchall()
            if len(d)==0:
                messagebox.showerror('error','wrong password or username')
            else:
                login=True
                messagebox.showinfo('WELCOME','Welcome back, "{}"'.format(use))
                submit_button.config(state=DISABLED)
                window.destroy()
                window1.destroy()
        else:
            messagebox.showerror('error','wrong password or username')
    username=Label(window,text='username')
    passwordl=Label(window,text='password')
    pas=Entry(window,bg='lightblue')
    user=Entry(window,bg='lightblue')
    submit_button=Button(window,
                         text='submit',
                         command=login,
                         state=ACTIVE)
    passwordl.pack()
    pas.pack()
    username.pack()
    user.pack()
    submit_button.pack()

    window.mainloop()
    

def sign():
    global window1
    signin_button.config(state=DISABLED)
    login_button.config(state=DISABLED)
    window=Tk()
    window.geometry("300x300")
    window.title("signin")
    window.config(background='White')
    def signin():
        passwd=pas.get()
        use=user.get()
        pas.delete(0,END)
        user.delete(0,END)
        if passwd.isdigit():
            q="Select password from udet where password={}".format(passwd)
            cuo.execute(q)
            d=cuo.fetchall()
            if len(d)>0:
                messagebox.showerror('error','please try another password')
            else:
                q="Select username from udet where username='{}'".format(use)
                cuo.execute(q)
                d=cuo.fetchall()
                if len(d)>0 or len(use)>20:
                    messagebox.showerror('error','please try another username with less than 20 characters')
                else:
                    q='insert into udet values({},"{}")'.format(passwd,use)
                    cuo.execute(q)
                    co.commit()
                    q='insert into ugame values("{}",0,0,0)'.format(use)
                    cuo.execute(q)
                    co.commit()
                    messagebox.showinfo('WELCOME','successfully signed in')
                    submit_button.config(state=DISABLED)
                    window.destroy()
                    window1.destroy()
                
        else:
            messagebox.showerror('error','please enter an integer as password')
    pas=Entry(window,bg='lightblue')
    user=Entry(window,bg='lightblue')
    submit_button=Button(window,
                         text='submit',
                         command=signin,
                         state=ACTIVE)
    username=Label(window,text='username')
    passwordl=Label(window,text='password')
    submit_button.pack()
    passwordl.pack()
    pas.pack()
    username.pack()
    user.pack()
    window.mainloop()

login_button=Button(window1,
                     text='login',
                     command=log,
                     state=ACTIVE)
signin_button=Button(window1,
                     text='signin',
                     command=sign,
                     state=ACTIVE)
login_button.pack()
signin_button.pack()
window1.mainloop()

if login:
    pygame.init()
    screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN) #screen
    clock=pygame.time.Clock() #clock

    class bg:
        
    
        x=800
        y=450
        up_enable=True #moving background layout up
        right_enable=True #moving background layout right
        left_enable=True #moving background layout left
        down_enable=True #moving background layout down
        vel=0 #gravity velocity
        grav_acc=.2 #acceleration due to gravity
    
        def __init__(self):
            self.bg=pygame.image.load("map_layout.png").convert_alpha() #import image
            self.bg=pygame.transform.rotozoom(self.bg,0,2) #transform size
            self.bg_rect=self.bg.get_rect(center=(bg.x,bg.y)) #rectangle
            self.bg_mask=pygame.mask.from_surface(self.bg) #mask

        
        @classmethod
        def up(cls):
            global px2,py2,b
            if cls.up_enable:
                cls.y+=3
                #py2+=3
                b+=3
        @classmethod
        def down(cls):
            global px2,py2,b
            if cls.down_enable:
                cls.y-=3
                #py2-=3
                b+=3
        @classmethod
        def right(cls):
            global px2,py2,a
            if cls.right_enable:
                cls.x-=5
                #px2-=200
                a-=5
        @classmethod
        def left(cls):
            global px2,py2,a
            if cls.left_enable:
                cls.x+=5
                #px2+=200
                a+=5
        
        def gravity(self):
            if bg.down_enable:
                bg.y-=self.vel
                self.vel+=self.grav_acc

        def blit(self,screen):
            self.bg_rect.center=(bg.x,bg.y)
            screen.blit(self.bg,self.bg_rect)

    class tempchar():
        x=px2
        y=py2
        @classmethod
        def update_coordinate(cls,px2,py2):
            cls.x=px2
            cls.y=py2
        def __init__(self):

            self.ptemprect_image=pygame.Surface((20,20)) #surface    ------temporary-------#################
            self.ptemprect_image.fill('Yellow') #fill red colour    ------temporary------##############
            #self.ptemprect_rect_image=self.ptemprect_image.get_rect(center=(background.x,background.y))
        def blit(self,screen,px2,py2):
            screen.blit(self.ptemprect_image,(px2+10,py2-0))

    char=tempchar()
        

    class background:
        
        x=800
        y=450
        up_enable=True #moving background layout up
        right_enable=True #moving background layout right
        left_enable=True #moving background layout left
        down_enable=True #moving background layout down
        vel=0*.5/3 #gravity velocity
        grav_acc=.2*.5/3 #acceleration due to gravity
        
        def __init__(self):
            self.image=pygame.image.load("background.png").convert_alpha() #import image
            self.image=pygame.transform.rotozoom(self.image,0,2) #transform size
            self.rect=self.image.get_rect(center=(background.x,background.y)) #rectangle
            
        @classmethod
        def up(cls):
            if cls.up_enable:
                cls.y+=.5
        @classmethod
        def down(cls):
            if cls.down_enable:
                cls.y-=.5
        @classmethod
        def right(cls):
            if cls.right_enable:
                cls.x-=5*.5/3
        @classmethod
        def left(cls):
            if cls.left_enable:
                cls.x+=5*.5/3
        
        def gravity(self):
            if background.down_enable:
                background.y-=self.vel
                self.vel+=self.grav_acc

        def blit(self,window):
            self.rect.center=(background.x,background.y)
            window.blit(self.image,self.rect)


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
        q='select * from ugame'
        cuo.execute(q)
        d=cuo.fetchall()
        text1=text_font.render(str([d[0][0],d[0][1],d[0][2],d[0][3]]),False,'Red')
        text2=text_font.render(str([d[1][0],d[1][1],d[1][2],d[1][3]]),False,'Red')
        text3=text_font.render(str([d[2][0],d[2][1],d[2][2],d[2][3]]),False,'Red')
        text4=text_font.render(str([d[3][0],d[3][1],d[3][2],d[3][3]]),False,'Red')
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
        screen.blit(text1,(500,700))
        screen.blit(text2,(500,400))
        screen.blit(text3,(500,500))
        screen.blit(text4,(500,600))
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
    def lost():
        instruction_text1=text_font.render('YOU LOST',False,'Red')

        screen.fill('Light blue')
        screen.blit(instruction_text1,(500,0))
    def lostm():    
        q='update ugame set game_lost=game_lost+1 where username="{}"'.format(use)
        cuo.execute(q)
        co.commit()
        q='update ugame set rating=game_won*100/(game_won+game_lost) where username="{}"'.format(use)
        cuo.execute(q)
        co.commit()
    def won():
        instruction_text1=text_font.render('YOU WON',False,'Red')

        screen.fill('Light blue')
        screen.blit(instruction_text1=font.render('YOU LOST',False,'Red'))

    def wonm():
        q='update ugame set game_won=game_won+1 where username="{}"'.format(use)
        cuo.execute(q)
        co.commit()
        q='update ugame set rating=game_won*100/(game_won+game_lost) where username="{}"'.format(use)
        cuo.execute(q)
        co.commit()

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

    test_font=pygame.font.Font(None,50)

    x=700
    y=450

    m=600
    n=50

    gs=0
    health=100

    sky_surface = pygame.image.load("background.png").convert_alpha()
    gun_surface = pygame.image.load("Untitled design (8).png").convert_alpha()
    gun_surface=pygame.transform.rotozoom(gun_surface,0,.1)
    gun_surface_rect=gun_surface.get_rect(center=(700,450))
    player_surface = pygame.image.load("Untitled design (8).png").convert_alpha()
    player_surface=pygame.transform.rotozoom(player_surface,0,0.1)
    text_surface=test_font.render('Reload!!',False,'Black')
    text_surface2=test_font.render('Reloading!!',False,'Black')
    text_surface3=test_font.render(f"Health: {health}",False,'Black')
    B1= pygame.image.load("Untitled design (7).png").convert_alpha()
    B1=pygame.transform.rotozoom(B1,0,.2)
    
    New_bullet=[B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1,B1]
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

        px1,py1=bg.x,bg.y
        
        p1_position = [px1,py1]  # str(main.px1,mainpy1)

        #print(p1_position)

        conn.send(bytes(str(p1_position), 'utf-8'))
        
        p2_position = conn.recv(1024).decode()
        p2_position = ast.literal_eval(p2_position)

        

        conn.send(bytes(str(health), 'utf-8'))
        health1=conn.recv(1024).decode()

        px2=p2_position[0]
        py2=p2_position[1]

        tempchar.update_coordinate(px2,py2)

        healthme=health1
        healthop=health
        
        if healthme=='opponent won':
            gs=1
        if healthop<0:
            gs=2
        
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

            
            tempchar.x=player_rect.x
            tempchar.y=player_rect.y
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                bg.left()
                background.left()
            if bg.down_enable==False:
                bg1.vel=0
                background1.vel=0

            #jump
            if (key[pygame.K_UP] or key[pygame.K_w]) and bg.down_enable==False and bg.up_enable:
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
            if key[pygame.K_RIGHT] or key[pygame.K_d]:
                bg.right()
                background.right()
            if bg.down_enable and jump_status==0:
                bg1.gravity()
                background1.gravity()

            if bg.y<(-350):
                gs=1

            background1.blit(screen)
            bg1.blit(screen)
            main_character1.blit(screen)
            char.blit(screen,bg.x-px2+685,bg.y-py2+440)


            if health>100:
                health=100

            if len(Bullet_list)<1:
                screen.blit(text_surface2,t2_rect)
                Bullet_list.extend(New_bullet)
                Used_list=[]

            if len(Bullet_list)<=5:
                Re_war=True

            if len(Bullet_list)>=11:
                Re_war=False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:  
                Bullet_list.extend(New_bullet)


            if len(Bullet_list)>0:
                screen.blit(pygame.transform.rotozoom(Bullet_list[0],0,.2),bullet_rect)

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
                bullet_rect.right+=15

            if player_rect.colliderect(bullet_rect) and not player_rect.colliderect(gun_surface_rect):
                if len(Bullet_list)>0:
                    Bullet_list.pop(0)
                if len(Bullet_list)>0:
                    screen.blit(Bullet_list[0],bullet_rect)
                health-=1
                health=math.floor(health)

            if bullet_rect.right>=1600:
                if len(Bullet_list)>0:
                    Used_list.append(Bullet_list[0])
                    if len(Bullet_list)>0:
                        Bullet_list.pop(0)
                    if len(Bullet_list)>0:
                        bullet_rect=Bullet_list[0].get_rect(topleft=(x,y))
                        screen.blit(Bullet_list[0],(x,y))
                bul_stat=False


        if gs==0:
            text_surface3=test_font.render(f"Health: {health1}",False,'Black')
        elif gs==1:
            text_surface3=test_font.render(f"Health: opponent won",False,'Black')
        elif gs==2:
            text_surface3=test_font.render(f"Health: opponent won",False,'Black')

        text_surface4=test_font.render(f"Opponent Health: {health}",False,'Black')
        
        screen.blit(text_surface3,t3_rect)
        screen.blit(text_surface4,(1000,0))
        screen.blit(gun_surface,(700,450))
        screen.blit(player_surface,player_rect)

        player_rect=player_surface.get_rect(topleft=(bg.x-px2+685,bg.y-py2+440))

        
        if game_status==0:
            menu()
        if game_status==2:
            instruction_screen()

        if gs==1:
            #lostm()
            gs=-1
        if gs==2:
            #wonm()
            gs=-2
        if gs==-1:
            lost()
        if gs==-2:
            won()


        pygame.display.update()

        clock.tick(tick) #clock speed
