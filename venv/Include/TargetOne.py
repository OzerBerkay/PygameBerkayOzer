import pygame
import sys
import math
import random

class TargetOne():
    ExposedEvent=pygame.event.Event(pygame.USEREVENT, attr1='TargetOneExposed')
    def __init__(self,screen):
        self.x=0
        self.y=0
        self.mx=random.randint(-1, 1) #x haraket yönü
        self.my=0 #y haraket yönü
        self.rd = random.randint(0, 2)  # bu random ile rastgele olan 3 balığımızı oluşturacağız ve özelliklerini belirleyeceğiz
        if self.rd==0:
            self.life=100
        elif self.rd==1:
            self.life=250
        elif self.rd==2:
            self.life=500
        width=screen.get_width()
        height=screen.get_height()
        self.y=random.randint(10,height-int(height/5))#10 ile ekran yüksekliği arasında bir konum oluştur
        if self.mx<0:
            self.rectangle=pygame.rect.Rect(int(width/20)/2,self.y+int(height/10)/2,int(width/25),int(height/15))#en sağdan çıkar,rastgele y, boyut,boyut
        else:
            self.rectangle = pygame.rect.Rect(width+int(width / 20) / 2, self.y + int(height / 10) / 2, int(width / 25),
                                              int(height / 15))
        self.flyImageOrder=0
        self.flyImages=[]

        if self.mx <0:
          if self.rd==0:
              for i in range(1, 4):
                  self.flyImages.append(pygame.transform.scale(pygame.image.load("images/png/Bombs/baliksag" + str(i) + ".png"),(self.rectangle[2], self.rectangle[3])))
          elif self.rd==1:
              for i in range(1, 4):
                  self.flyImages.append(pygame.transform.scale(pygame.image.load("images/png/Bombs/balik2sag" + str(i) + ".png"),(self.rectangle[2], self.rectangle[3])))
          elif self.rd==2:
              for i in range(1, 4):
                  self.flyImages.append(pygame.transform.scale(pygame.image.load("images/png/Bombs/balik3sag" + str(i) + ".png"),(self.rectangle[2], self.rectangle[3])))


        else:
            if self.rd == 0:
                for i in range(1, 4):
                    self.flyImages.append(pygame.transform.scale(pygame.image.load("images/png/Bombs/baliksol" + str(i) + ".png"),(self.rectangle[2], self.rectangle[3])))
            elif self.rd == 1:
                for i in range(1, 4):
                    self.flyImages.append(pygame.transform.scale(pygame.image.load("images/png/Bombs/balik2sol" + str(i) + ".png"),(self.rectangle[2], self.rectangle[3])))
            elif self.rd == 2:
                for i in range(1, 4):
                    self.flyImages.append(pygame.transform.scale(pygame.image.load("images/png/Bombs/balik3sol" + str(i) + ".png"),(self.rectangle[2], self.rectangle[3])))


        self.explosionImageOrder=-1
        self.explosionImages=[]
        for i in range(1,10):
            self.explosionImages.append(pygame.transform.scale(pygame.image.load("images/png/Bombs/Bomb_1_Expo ("+str(i)+").png"),(self.rectangle[2]*4,self.rectangle[2]*4)))
        self.exposed=False



    def draw(self,screen):
        if self.explosionImageOrder==-1:
            self.flyImageOrder=(self.flyImageOrder+1)%3
            if self.rd==0:
                self.rectangle[0]=self.rectangle[0]-self.mx*2
            if self.rd==1:
                self.rectangle[0] = self.rectangle[0] - self.mx * 5
            if self.rd == 2:
                    self.rectangle[0] = self.rectangle[0] - self.mx * 9
            #self.rectangle[1]=self.rectangle[1]-self.my*2
            #self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            screen.blit(self.flyImages[self.flyImageOrder], [self.rectangle[0]-int(self.flyImages[self.flyImageOrder].get_width()/2),self.rectangle[1]-int(self.flyImages[self.flyImageOrder].get_height()/2)])
        else:
            self.explosionImageOrder=(self.explosionImageOrder+1)%9
            #self.rectangle[0]=self.rectangle[0]-self.mx*2
            #self.rectangle[1]=self.rectangle[1]-self.my*2
            self.rectangle.centerx= self.rectangle.centerx-self.mx*6
            if self.explosionImageOrder==8:
                return True
            screen.blit(self.explosionImages[self.explosionImageOrder], [self.rectangle[0]-int(self.explosionImages[self.explosionImageOrder].get_width()/2),self.rectangle[1]-int(self.explosionImages[self.explosionImageOrder].get_height()/2)])
            if self.explosionImageOrder==8:
                self.explosionImageOrder=-1

        return False
    def hit(self):
        self.life= self.life-50
        if self.life<=0:
            self.expose()
            
    def expose(self):
        self.life=0
        self.exposed=True
        if self.explosionImageOrder<0:
            self.explosionImageOrder=0

            
            
