import pygame
import sys
import math
import random
dest = True

class Bullet():
    def __init__(self,plane,mx,yol):
        self.x=0
        self.y=0
        self.mx=mx #x haraket yönü
        self.my=0 #x haraket yönü
        global dest
        dest=yol
        if dest is True:
            self.mx=-1
        else:
            self.mx=1
        print(self.mx)
        self.rectangle=pygame.rect.Rect(plane.rectangle[0] + int(plane.rectangle[2]/12*11), plane.rectangle[1] +  int(plane.rectangle[3]/12*4), int(plane.rectangle[2] / 5), int(plane.rectangle[3] / 5))
        self.imageOrder=0
        self.images=[pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (1).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (2).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (3).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (4).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (5).png"),(self.rectangle[2],self.rectangle[3]))]
    def draw(self,screen):
        print(dest)

        if dest is True or self.mx==-1:
            self.rectangle[0] = self.rectangle[0] + self.mx * 40
            self.imageOrder = (self.imageOrder + 1) % 5
            screen.blit(self.images[self.imageOrder], self.rectangle)
        elif dest is False or self.mx==1:
            self.rectangle[0] = self.rectangle[0] + self.mx * 40
            self.imageOrder = (self.imageOrder + 1) % 5
            screen.blit(self.images[self.imageOrder], self.rectangle)



        #self.rectange.clamp_ip(screen.get_rect())
        ##mermi objesini ekran karesi içinden çıkarsa silinir
        ##bunu planeden kontrol edeceğiz.



