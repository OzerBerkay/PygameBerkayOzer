import pygame

class AirBoard:
    air=100
    time=0
    @staticmethod
    def init_AirBoard(rectangle=pygame.rect.Rect(400,20,1800,50),textSize=40,textColor=(235,247,9)):
        AirBoard.textSize=textSize
        AirBoard.textColor=textColor
        AirBoard.rectangle=rectangle


    @staticmethod
    def set_Air(air):
        if air==1: #gönderilen koşullara göre oyun baştan başlayacaksa 100 eğer hava kutusu aldıysa +2 eğer herhangi bir durum oluşmadıysa herhangi bir
            AirBoard.air=100 #sayı gönderilirsa hava azalacak
        elif air==2:
            if AirBoard.air+20<=100:
                AirBoard.air+=20
        else:

            AirBoard.air-=1
        if(AirBoard.air<0):
            AirBoard.air=0

        AirBoard.air_fontedText=pygame.font.Font("fonts/ARCADE.TTF",AirBoard.textSize).render("Kalan hava:"+str(AirBoard.air),True,AirBoard.textColor)
        AirBoard.air_textRectangle=pygame.rect.Rect(0,0,AirBoard.air_fontedText.get_width(),AirBoard.air_fontedText.get_height())
        AirBoard.air_textRectangle.center=AirBoard.rectangle.center

    @staticmethod
    def get_Air():
        return AirBoard.air

    @staticmethod
    def draw(screen):
        screen.blit(AirBoard.air_fontedText,AirBoard.air_textRectangle)