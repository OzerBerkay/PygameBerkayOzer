import pygame
import sys
import math
import random
from  threading import Timer
from TargetOne import TargetOne
from Plane import Plane
from Bullet import Bullet
from pTimer import  pTimer
from AirBoard import AirBoard
from AirOne import AirOne

#Burada oluşacak hava kutularına süre atamak için ve kalan havamızı her seferinde güncellemek için gerekli olan kodları oluşturduk
class ChapterOne():
    def __init__(self,screen):
        self.name="Let's Start"
        self.plane= Plane(screen)
        self.targets=[]
        self.airs=[]
        self.backGroundImage=pygame.transform.scale(pygame.image.load("images/png/BG.png"),(screen.get_width(), screen.get_height()))
        self.backGroundImageX=0
        self.backGroundImageY=0
        self.screen = screen

        #2 saniyede bir hedef üretilmeli+

        #bunun için kendi yazdığımız timer sınıfını kulllıyoruz
        #bu işlem için uygun olan threadlerdir ancak bu konuya sonra geleceğiz
        self.pgenerateTargetTimer=pTimer(2,self.generateTarget,screen)
        self.pgenerateAirTimer = pTimer(15, self.generateAir, screen)  #hava kutuları için timer
        self.pgenerateAirBoardTimer=pTimer(1,self.generateAirTime,screen) #kalan hava için timer

        self.finishEvent=pygame.event.Event(pygame.USEREVENT, attr1='finishEvent')

    def start(self,screen):

        self.pgenerateTargetTimer.start()
        self.pgenerateAirTimer.start()
        self.pgenerateAirBoardTimer.start()

    def finish(self,screen):
        self.pgenerateTargetTimer.stop()
        self.pgenerateAirTimer.stop()
        self.pgenerateAirBoardTimer.stop()
        pygame.event.post(self.finishEvent)
        return True


    def generateTarget(self,arguments):
        newTarget= TargetOne(arguments[0])
        self.targets.append(newTarget)
    def generateAir(self,args):
        newAir=AirOne(args[0])
        self.airs.append(newAir)
    def generateAirTime(self,cd):
        if AirBoard.get_Air()<=0:
            AirBoard.set_Air(False)
            self.plane.expose()
            self.finish(self.screen)

        AirBoard.set_Air(False)

    def drawTime(self,screen):
        AirBoard.draw(screen);


    def drawBackGround(self, screen):
        screen.blit(self.backGroundImage,(self.backGroundImageX,0))
        self.backGroundImageX=self.backGroundImageX-1
        screen.blit(self.backGroundImage,(screen.get_width()+self.backGroundImageX,0))
        #resim dönüşünde x değerini sıfırlıyoruz
        if screen.get_width() == -self.backGroundImageX:
            self.backGroundImageX=0

    def drawPlane(self,screen):
        self.plane.draw(screen)




    def drawTargets(self,screen):
        for target in self.targets:
            exposed=target.draw(screen)
            if exposed:
                self.targets.remove(target)
                pygame.event.post(TargetOne.ExposedEvent)
                if self.plane.exposed:
                    pygame.event.post(self.plane.exposedEvent)
                    self.finish(screen)

            else:
                if target.rectangle.colliderect(self.plane.rectangle):
                    if not target.exposed:
                        target.expose()
                        self.plane.expose()

                else:
                    for bullet in self.plane.bullets:
                        #eğer eşleşme varsa
                        if target.rectangle.colliderect(bullet.rectangle):
                            #target hit almış demektir.
                            target.hit()
                            #mermi kaybolmalı
                            self.plane.bullets.remove(bullet)
    def drawAirs(self,screen):
        for air in self.airs:
            exposed=air.draw(screen)
            if exposed:
                self.airs.remove(air)
                pygame.event.post(AirOne.ExposedEvent)
                if self.plane.exposed:
                    pygame.event.post(self.plane.exposedEvent)
                    self.finish(screen)

            else:
                for bullet in self.plane.bullets:
                    #eğer eşleşme varsa
                    if air.rectangle.colliderect(bullet.rectangle):
                        #air hit almış demektir.
                        air.hit()
                        #mermi kaybolmalı
                        self.plane.bullets.remove(bullet)



    def draw(self,screen):
        self.drawBackGround(screen)
        self.drawPlane(screen)
        self.drawTargets(screen)
        self.drawTime(screen);
        self.drawAirs(screen)
