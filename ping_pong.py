import pygame
import random

pygame.init()

print("This is a ping-pong game. \nControls: \nUp: Player_1: 'w' or Player_2:'o' \nDown: Player_1:'s' or Player_2:'k'")
player_1_name = input("Choose a name for Player_1: ")
player_2_name = input("Choose a name for Player_2: ")

#felugro ablak meret
WIDTH, HEIGHT = 1000, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong Game")
run = True
player_1 = player_2 = 0
direction = [0, 1] #labda irányának randomizálásához két érték
angle = [0, 1, 2] #labda szögének randomizálásához két érték
                    # a x és y sebességének változtatásával elérjük a különböző szögeket
                    # 0 -> y = 2x | 1 -> y = x | 2 -> x = 2y
                    # ezután a szervacserénél kell mókolni mert ott indul ujra a  
#használt színkódok
MAG = (234, 10, 142)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#labda méretei
radius = 15 #nagyság
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius #x,y tengely pozicio
ball_speed_x, ball_speed_y = 0.6, 0.6 #mozgási sebesség

#ütők méretei
rocket_width, rocket_height = 20, 120
left_rocket_x, right_rocket_x = 100 - rocket_width/2, WIDTH - (100 - rocket_width/2)
left_rocket_y = right_rocket_y = HEIGHT/2 - rocket_height/2
right_rocket_speed = left_rocket_speed = 0 #ütők kezdeti sebessége 0

while run:
    #a képernyő kitöltése feketével majd újrarajzolás h ne hagyjon nyomot a labda ahogy mozog
    win.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN: #billentyűzet check funkció
            if i.key == pygame.K_o: #ha a felfelé gombot megnyomod...
                right_rocket_speed = -0.9 # az y tengelyen kivonjuk az ütő helyzetét így felmegy
            if i.key == pygame.K_k:
                right_rocket_speed = 0.9
            if i.key == pygame.K_w: #másik oldal, a felfelé itt a w billentyű a lefelé az s
                left_rocket_speed = -0.9
            if i.key == pygame.K_s:
                left_rocket_speed = 0.9
        
        if i.type == pygame.KEYUP: #ha felemeled a gombról a kezed megálljon a mozgás
            right_rocket_speed = 0
            left_rocket_speed = 0


    #a labda visszapattanjon az y tengelyről
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_speed_y *= -1 #megforditjuk a sebességet
        

    #jobb oldalon megy ki a labda (szervacsere)
    if ball_x >= WIDTH - radius:
        player_1 += 1
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius  #labda kezdő poziciója
        dir = random.choice(direction)
        ang = random.choice(angle)
        #szögek, irány változtatásához tartozó feltételek (dir 0,1 | ang 0,1,2)
        if dir ==0: 
            if ang == 0:
                ball_speed_y, ball_speed_x = -0.8, 0.4
            if ang == 1:
                ball_speed_y, ball_speed_x = -0.4, 0.4
            if ang  == 2:
                ball_speed_y, ball_speed_x = -0.4, 0.8
        if dir == 1: 
            if ang == 0:
                ball_speed_y, ball_speed_x = 0.8, 0.4
            if ang == 1:
                ball_speed_y, ball_speed_x = 0.4, 0.4
            if ang  == 2:
                ball_speed_y, ball_speed_x = 0.4, 0.8
      

    #bal oldalon megy ki a labda (szervacsere)
    if ball_x <= 0 + radius:
        player_2 += 1
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        #szögek, irány változtatásához tartozó feltételek (dir 0,1 | ang 0,1,2)
        if dir ==0: 
            if ang == 0:
                ball_speed_y, ball_speed_x = -0.5, 0.25
            if ang == 1:
                ball_speed_y, ball_speed_x = -0.25, 0.25
            if ang  == 2:
                ball_speed_y, ball_speed_x = -0.25, 0.5
        if dir == 1: 
            if ang == 0:
                ball_speed_y, ball_speed_x = 0.5, 0.25
            if ang == 1:
                ball_speed_y, ball_speed_x = 0.25, 0.25
            if ang  == 2:
                ball_speed_y, ball_speed_x = 0.25, 0.5
   

     #az ütők ne menjenek ki a "pályáról"
    if left_rocket_y >= HEIGHT - rocket_height:
        left_rocket_y = HEIGHT - rocket_height
    if left_rocket_y <= 0:
        left_rocket_y = 0
    
    if right_rocket_y >= HEIGHT - rocket_height:
        right_rocket_y = HEIGHT - rocket_height
    if right_rocket_y <= 0:
        right_rocket_y = 0

    #labda ütközik az ütővel
    #bal oldal (ütő pozija a rácson <=  labda pozija a rácson <= (ütő pozija a rácson + ütő szélessége))
    #hozzá kell adni az ütő szélességét is h a belső oldaláról pattanjon vissza
    if left_rocket_x <= ball_x <= left_rocket_x + rocket_width:
        if left_rocket_y <= ball_y <= left_rocket_y + rocket_height: #y tengelyen is vizsgálod
            ball_x = left_rocket_x + rocket_width #az ütő széléről (pozi + maga az ütő vastagsága)
            ball_speed_x *= -1 #megforditjuk az irányt

    #ugyanez majdnem a jobb oldalon csak nem kell az ütő vastagsága
    #(mivel a rács origója a bel felső sarokban van)
    if right_rocket_x <= ball_x <= right_rocket_x + rocket_width:
        if right_rocket_y <= ball_y <= right_rocket_y + rocket_height: #y tengelyen is vizsgálod
            ball_x = right_rocket_x #az ütő széléről (pozi + maga az ütő vastagsága)
            ball_speed_x *= -1

    #a labda és az ütők mozgatása
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    right_rocket_y += right_rocket_speed
    left_rocket_y += left_rocket_speed

    #pontok kiírása
    font = pygame.font.SysFont('callibiri', 30)
    score = font.render(player_1_name + ": " + str(player_1), True, WHITE) #betűtípus,szín
    win.blit(score, (30,30))
    score = font.render(player_2_name+ ": " + str(player_2), True, WHITE) #betűtípus,szín
    win.blit(score, (830,30))

    #a labda és az ütők kirajzolása
    pygame.draw.circle(win, MAG, (ball_x, ball_y), radius)
    pygame.draw.rect(win, WHITE, pygame.Rect(left_rocket_x, left_rocket_y, rocket_width, rocket_height))
    pygame.draw.rect(win, WHITE, pygame.Rect(right_rocket_x, right_rocket_y, rocket_width, rocket_height))
    pygame.display.update()

    # záró képernyő
    winner = pygame.font.SysFont('callibri', 110)
    if player_1 >= 3:
        win.fill(BLACK) #kitölti feketével a képernyőt
        endscreen = winner.render(player_1_name + " WON!!", True, RED)
        win.blit(endscreen, (200, 250))
        pygame.display.update()
        pygame.time.wait(3000)
        run = False

    if player_2 >= 3:
        win.fill(BLACK) #kitölti feketével a képernyőt
        endscreen = winner.render(player_2_name + " WON!!", True, RED)
        win.blit(endscreen, (200, 250))
        pygame.display.update()
        pygame.time.wait(3000)
        run = False