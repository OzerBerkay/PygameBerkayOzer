import pygame
import sys
import math
import random

#Burada hava kutusu görselini yukarıya doğru götürmeyi sağladık.
class AirOne():
    ExposedEvent = pygame.event.Event(pygame.USEREVENT, attr1='AirOneExposed')

    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.mx = 0  # x haraket yönü
        self.my = 1 # y haraket yönü
        self.life = 100
        width = screen.get_width()
        height = screen.get_height()
        self.x = random.randint(10, width - int(width / 5))  #10 ile genişlik arasında kutu oluşturacağız
        self.rectangle = pygame.rect.Rect(self.x + int(height / 20) / 2, width+ int(width / 10) / 2, int(width / 20),
                                          int(height / 10))

        self.flyImageOrder = 0
        self.flyImages = []

        self.flyImages.append(
            pygame.transform.scale(pygame.image.load("images/png/Bombs/air.png"),
                                   (self.rectangle[2], self.rectangle[3])))

        self.explosionImageOrder = -1
        self.explosionImages = []
        for i in range(1, 10):
            self.explosionImages.append(
                pygame.transform.scale(pygame.image.load("images/png/Bombs/Bomb_1_Expo (" + str(i) + ").png"),
                                       (self.rectangle[2] * 4, self.rectangle[2] * 4)))
        self.exposed = False

    def draw(self, screen):                     #yalnızca mermi çarparsa patlayacak kişi çarparsa değil
        if self.explosionImageOrder == -1:
            self.flyImageOrder = (self.flyImageOrder + 1)%1
            #self.rectangle[0] = self.rectangle[0] - self.mx * 2
            self.rectangle[1]=self.rectangle[1]-self.my*15
            # self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            screen.blit(self.flyImages[self.flyImageOrder],
                        [self.rectangle[0] - int(self.flyImages[self.flyImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.flyImages[self.flyImageOrder].get_height() / 2)])
        else:
            self.explosionImageOrder = (self.explosionImageOrder + 1) % 9
            # self.rectangle[0]=self.rectangle[0]-self.mx*2
            # self.rectangle[1]=self.rectangle[1]-self.my*2
            self.rectangle.centerx = self.rectangle.centerx - self.mx * 2
            if self.explosionImageOrder == 8:
                return True
            screen.blit(self.explosionImages[self.explosionImageOrder],
                        [self.rectangle[0] - int(self.explosionImages[self.explosionImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.explosionImages[self.explosionImageOrder].get_height() / 2)])
            if self.explosionImageOrder == 8:
                self.explosionImageOrder = -1

        return False

    def hit(self):
        self.life = self.life - 50
        if self.life <= 0:
            self.expose()

    def expose(self):
        self.life = 0
        self.exposed = True
        if self.explosionImageOrder < 0:
            self.explosionImageOrder = 0