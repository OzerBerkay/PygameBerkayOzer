import pygame
import sys
import math
import random
from Bullet import Bullet



yol = False
class Plane():

    def __init__(self,screen):
        self.x=0
        self.y=0
        self.mx=0 #x haraket yönü
        self.my=0 #x haraket yönü



        width=screen.get_width()
        height=screen.get_height()
        self.rectangle=pygame.rect.Rect(450,1500,int(width/20),int(height/20))
        self.flyImageOrder=0
        #buradaki kodlarda sağa ve sola dönmesii durumunda, ateş etmesi ve yaralanması durumunda gerekli olan png leri yükledik
        self.flyImages=[pygame.transform.scale(pygame.image.load("images/png/Plane/1yuz.png"), (self.rectangle[2], self.rectangle[3])), pygame.transform.scale(pygame.image.load("images/png/Plane/2yuz.png"), (self.rectangle[2], self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/3yuz.png"), (self.rectangle[2], self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/4yuz.png"), (self.rectangle[2], self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/5yuz.png"), (self.rectangle[2], self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/6yuz.png"), (self.rectangle[2], self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/7yuz.png"), (self.rectangle[2], self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/1yuzsol.png"),
                                                     (self.rectangle[2], self.rectangle[3])),
                              pygame.transform.scale(pygame.image.load("images/png/Plane/2yuzsol.png"),
                                                     (self.rectangle[2], self.rectangle[3])),
                              pygame.transform.scale(pygame.image.load("images/png/Plane/3yuzsol.png"),
                                                     (self.rectangle[2], self.rectangle[3])),
                              pygame.transform.scale(pygame.image.load("images/png/Plane/4yuzsol.png"),
                                                     (self.rectangle[2], self.rectangle[3])),
                              pygame.transform.scale(pygame.image.load("images/png/Plane/5yuzsol.png"),
                                                     (self.rectangle[2], self.rectangle[3])),
                              pygame.transform.scale(pygame.image.load("images/png/Plane/6yuzsol.png"),
                                                     (self.rectangle[2], self.rectangle[3])),
                              pygame.transform.scale(pygame.image.load("images/png/Plane/7yuzsol.png"),
                                                     (self.rectangle[2], self.rectangle[3]))]





        self.shootImageOrder=0
        self.shootImages=[pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot1.png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot2.png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot3.png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot4.png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot5.png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot6.png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot7.png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot1sol.png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot2sol.png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot3sol.png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot4sol.png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot5sol.png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot6sol.png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Plane/Shoot7sol.png"),(self.rectangle[2],self.rectangle[3]))]
        self.exposedImage=pygame.transform.scale(pygame.image.load("images/png/Plane/hurt.png"), (self.rectangle[2], self.rectangle[3]))

        self.bullets=[]
        self.exposed=False
        self.exposedEvent=pygame.event.Event(pygame.USEREVENT, attr1='planeExposedEvent')


    def draw(self,screen):

        if self.exposed:
            screen.blit(self.exposedImage, self.rectangle)
            return True
        global yol                      #burada yukarıdaki yolu statik gibi kullanacağız ve gelen yön bilgisine göre güncelleyeceğiz. Buna gerek duyduk çünkü mx 0 olduğu durumda dahi bir önceki
                                        #konumunu korusun
        if  self.mx==-1:
            yol=True
        if self.mx==1:
            yol=False

        self.rectangle[0]=self.rectangle[0]+self.mx*10
        self.rectangle[1]=self.rectangle[1]+self.my*10
        self.rectangle.clamp_ip(screen.get_rect())# plane objesini ekran karesi içinde tutar
        if self.shootImageOrder==-1:                                                #burada ateşlenip ateşlenmediği durumlar için içlerinde yön kontrolü yaparak seçili yönde yüzüp
            if yol==False:                                                          #seçili yöne ateş etme animasyonu sağlanmıştır.
                self.flyImageOrder=(self.flyImageOrder+1)%7

                screen.blit(self.flyImages[self.flyImageOrder], self.rectangle)
            elif yol==True:
                self.flyImageOrder=(self.flyImageOrder+1)%7+7
                screen.blit(self.flyImages[self.flyImageOrder], self.rectangle)
        else:
            if yol==False:

                screen.blit(self.shootImages[self.shootImageOrder], self.rectangle)
                self.shootImageOrder = self.shootImageOrder + 1
                if self.shootImageOrder==5:
                    self.shootImageOrder=-1

            else:
                self.shootImageOrder =( self.shootImageOrder + 1)%7 + 7
                screen.blit(self.shootImages[self.shootImageOrder], self.rectangle)
                if self.shootImageOrder == 13:
                    self.shootImageOrder = -1


        for bullet in self.bullets:
            bullet.draw(screen)
            #rectangle sınıfının contains fonsiyonu dörtgenin diğerinin içinde olup olmadığı bilgisini döndürür.
            #biz burada mermiler ekrandan çıkmışmı kontrolü yapacağız
            #ekrandan çıkan mermiler mermi listesinden silinmeli, aksi taktirde binlerce mermi sonsuzluğa kadar gider bu da boşa kaynak sarfıdır.
            if not screen.get_rect().contains(bullet.rectangle):
                self.bullets.remove(bullet) #foreach döngülerinde bunu yapmak iyi bir yöntem değildir, çünkü dizin bozulur. Bir çok programlama dilinde hata alırsınız.
                                            #ancak burada python kabul etti :D
    def fire(self,screen):


        nbullet=Bullet(self,self.mx,yol)
        #nbullet.mx=self.mx
        self.bullets.append(nbullet)
        #her ateş edilişinde bir ateş edilme animasyonu devreye girmelidir
        #bu işlem farklı yollarla yapılabilir
        # burada yaprığımız normalde -1 olan shoot değerini 0  yapıyoruz ve nesnenin çizim fonksiyonunda bir if yapısıyla bu durumu kontrol ediyoruz.
        self.shootImageOrder=0

    def expose(self):
        self.exposed=True

