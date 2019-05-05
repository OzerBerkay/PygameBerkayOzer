#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
import pygame
import sys
import math
import random

from Chapter import ChapterOne
from Menu import Menu
from ScoreBoard import ScoreBoard
from TargetOne import  TargetOne
from AirBoard import AirBoard
from AirOne import AirOne


pygame.init()
clock = pygame.time.Clock()
endEvent = pygame.event.Event(pygame.USEREVENT, attr1='endEvent')
AirBoard.init_AirBoard()
AirBoard.set_Air(1)
def GameLoop():



    gameDisplay_width = 1500
    gameDisplay_height = 900
    gameDisplay = pygame.display.set_mode((gameDisplay_width, gameDisplay_height))
    pygame.display.set_caption('Gamemaker')

    crashed = False

    chapter = ChapterOne(gameDisplay)
    chapter.start(gameDisplay)

    menu = Menu(gameDisplay.get_rect())
    end = False
    ScoreBoard.init_ScoreBoard()
    ScoreBoard.set_Score(0)


    while not crashed:

        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    chapter.pgenerateTargetTimer.pause(True)
                    chapter.pgenerateAirBoardTimer.pause(True)
                    chapter.pgenerateAirTimer.pause(True)
                    crashed=menu.runMenu(gameDisplay)
                    if crashed=="restart":                       #eğer resete basarsak havamız sıfırlansın eğer esc ye basarsak tüm sayaçlar ve oyun dursun
                        AirBoard.set_Air(1)
                        crashed=True #burada önceki loop u durdurduk
                        GameLoop()   #yeni bir loop ile oyunu başlattık
                    chapter.pgenerateTargetTimer.pause(False)
                    chapter.pgenerateAirBoardTimer.pause(False)
                    chapter.pgenerateAirTimer.pause(False)

                if event.key == pygame.K_UP:
                    chapter.plane.my=-1




                if event.key == pygame.K_DOWN:
                    chapter.plane.my=1
                if event.key == pygame.K_LEFT:
                    chapter.plane.mx=-1

                if event.key == pygame.K_RIGHT:
                    chapter.plane.mx=1

                if event.key == pygame.K_SPACE:
                    chapter.plane.fire(gameDisplay)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    chapter.plane.my=0
                if event.key == pygame.K_DOWN:
                    chapter.plane.my=0
                if event.key == pygame.K_LEFT:
                    chapter.plane.mx=0
                if event.key == pygame.K_RIGHT:
                    chapter.plane.mx=0
            #event karşılaştırmalarında eşitlik koşulu çalışır
            #eventlar aynı olmalı özellikleriyle birlikte
            elif event== chapter.finishEvent:
                print(event)
                end=True
            elif event==TargetOne.ExposedEvent:
                ScoreBoard.set_Score(10)
            elif event==AirOne.ExposedEvent:        #hava kutusunu aldık +20 hava
                AirBoard.set_Air(2)


            elif event== chapter.plane.exposedEvent:
                print(event)



        if not end:
            chapter.draw(gameDisplay)
            ScoreBoard.draw(gameDisplay)
            AirBoard.draw(gameDisplay)




        pygame.display.update()
        clock.tick(15)

    pygame.quit()
    quit()

GameLoop()