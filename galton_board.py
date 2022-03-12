##############################
#                            #
#                            #
#                            #
#          made by           #
#       Levin Ayrilmaz       #
#           2022             #
#                            #
#                            #
##############################

# https://github.com/levinayrilmaz/galton-board-py #


import pygame
from pygame.locals import *
import random

pygame.init()

ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

FENSTERBREITE = 640
FENSTERHOEHE = 700

anzahl_ball = [0, 0, 0, 0, 0, 0, 0, 0, 0]

DING1 = True
DING2 = True
DING3 = True
DING4 = True

screen = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))

windowSurface = pygame.display.set_caption("Galton-Board (made by Levin Ayrilmaz)")
spielaktiv = True

clock = pygame.time.Clock()


anzahl_der_baelle = 100

ballpos_x = []
ballpos_y = []
LEFT = []
RIGHT = []
for i in range(anzahl_der_baelle):
    ballpos_x.append((FENSTERBREITE/2)-5)
    ballpos_y.append(20)
    LEFT.append(False)
    RIGHT.append(False)


BALL_DURCHMESSER = 15

started = False



while spielaktiv:

    if started:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                spielaktiv = False

        screen.fill(SCHWARZ)


        baelle = []
        
        for i in range(len(ballpos_x)):
            baelle.append(pygame.draw.ellipse(screen, ROT, [ballpos_x[i], ballpos_y[i], BALL_DURCHMESSER, BALL_DURCHMESSER]))


        ding1 = pygame.draw.rect(screen, WEISS, [(FENSTERBREITE/2), 100, 5, 20])

        dinger = []
        for r in range(8):
            for i in range(r+2):
                dinger.append(pygame.draw.rect(screen, WEISS, [(FENSTERBREITE/100)*((45-r*5)+i*10), 150+r*50, 5, 20]))



        border_y=500
        border_laenge=100
        for i in range(9):
            pygame.draw.rect(screen, WEISS, [(FENSTERBREITE/100)*(8+i*10), border_y, 5, border_laenge])
            pygame.draw.rect(screen, WEISS, [(FENSTERBREITE/100)*(12+i*10), border_y, 5, border_laenge])
        

        for i in range(8):
            pygame.draw.rect(screen, WEISS, [(FENSTERBREITE/100)*(12+i*10), border_y, 44, 5])
        
        for i in range(8):
            pygame.draw.rect(screen, WEISS, [(FENSTERBREITE/100)*(12+i*10), border_y+95, 44, 5])
        

        for i in range(len(ballpos_y)):
            if ballpos_y[i] <= 25:
                ballpos_y[i] += 10
                RIGHT[i] = False
                LEFT[i] = False

            elif ballpos_y[i] <=550:
                vel = 1
                if RIGHT[i]==False and LEFT[i]==False:
                    ballpos_y[i] += 10 * vel
                
                if RIGHT[i]==True and LEFT[i]==False:
                    ballpos_y[i] += 2 * vel
                    ballpos_x[i] += 1.3

                if RIGHT[i]==False and LEFT[i]==True:
                    ballpos_y[i] +=2 * vel
                    ballpos_x[i] -= 1.3
            else:
                ballpos_y[i] += 10

                DING1 = True

                ding = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]


                if ballpos_x[i] < (FENSTERBREITE/100)*15:
                    anzahl_ball[0] += 1
                elif ballpos_x[i] < (FENSTERBREITE/100)*25:
                    anzahl_ball[1] += 1
                elif ballpos_x[i] < (FENSTERBREITE/100)*35:
                    anzahl_ball[2] += 1
                elif ballpos_x[i] < (FENSTERBREITE/100)*45:
                    anzahl_ball[3] += 1
                elif ballpos_x[i] < (FENSTERBREITE/100)*55:
                    anzahl_ball[4] += 1
                elif ballpos_x[i] < (FENSTERBREITE/100)*65:
                    anzahl_ball[5] += 1
                elif ballpos_x[i] < (FENSTERBREITE/100)*75:
                    anzahl_ball[6] += 1
                elif ballpos_x[i] < (FENSTERBREITE/100)*85:
                    anzahl_ball[7] += 1
                elif ballpos_x[i] < (FENSTERBREITE/100)*95:
                    anzahl_ball[8] += 1


                

                ballpos_x[i] = (FENSTERBREITE/2)-5
                ballpos_y[i] = 20


        for r in range(len(baelle)):
            if ding1.colliderect(baelle[r]):
                a = random.randint(0,1)
                if(a==0):
                    LEFT[r]=True
                    RIGHT[r]=False
                else:
                    LEFT[r]=False
                    RIGHT[r]=True

        def direction(s):
            a = random.randint(0,1)
            if(a==0):
                LEFT[s]=True
                RIGHT[s]=False
            else:
                LEFT[s]=False
                RIGHT[s]=True


        for s in range(len(baelle)):
            for i in range(len(dinger)):
                if dinger[i].colliderect(baelle[s]):
                    if i < 3:
                        direction(s)
                    elif i < 6:
                        direction(s)
                    elif i < 10:
                        direction(s)
                    elif i < 15:
                        direction(s)
                    elif i < 21:
                        direction(s)
                    elif i < 28:
                        direction(s)
                    elif i < 36:
                        direction(s)
                    elif i < 44:
                        LEFT[s]=False
                        RIGHT[s]=False

        
        for i in range(9):
            ausgabetext = str(anzahl_ball[i])
            font = pygame.font.SysFont(None, 40)
            text = font.render(ausgabetext, True, ROT)
            text_rect = text.get_rect(center=((FENSTERBREITE/100)*(10.5+i*10), 630))
            screen.blit(text, text_rect) 
        
        ausgabetext = "number of balls: "+str(anzahl_der_baelle)
        font = pygame.font.SysFont(None, 30)
        text = font.render(ausgabetext, True, ROT)
        text_rect = text.get_rect(center=((FENSTERBREITE/100)*20, 50))
        screen.blit(text, text_rect) 

    else:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                spielaktiv = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x <= mouse[0] <= x+140 and y <= mouse[1] <= y+40:
                    started = True

        screen.fill(SCHWARZ)

        mouse = pygame.mouse.get_pos()
        x = FENSTERBREITE/2 - 100
        y = FENSTERHOEHE/2 - 30

        if x <= mouse[0] <= x+140 and y <= mouse[1] <= y+40:
            pygame.draw.rect(screen,ROT,[x,y,200,40])
            
        else:
            pygame.draw.rect(screen,ORANGE,[x,y,200,40])
        

        smallfont = pygame.font.SysFont('Corbel',35)
  

        text = smallfont.render('Starten' , True , WEISS)
        text_rect = text.get_rect(center=(FENSTERBREITE/2,FENSTERHOEHE/2-10))
        screen.blit(text, text_rect)

        ausgabetext = "Galton-Board"
        font = pygame.font.SysFont(None, 100)
        text = font.render(ausgabetext, True, WEISS)
        text_rect = text.get_rect(center=((FENSTERBREITE/100)*(50), 200))
        screen.blit(text, text_rect) 

        ausgabetext = "made by Levin Ayrilmaz"
        font = pygame.font.SysFont(None, 40)
        text = font.render(ausgabetext, True, WEISS)
        text_rect = text.get_rect(center=((FENSTERBREITE/100)*(50), 250))
        screen.blit(text, text_rect) 

        
        
        


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
