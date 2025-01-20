import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT=pygame.USEREVENT+1
BACKGROUND_COLOR_CHANGE_EVENT=pygame.USEREVENT+2
#background colors
blue=pygame.color('blue')
yellow=pygame.color('yellow')
navy_blue=pygame.color('navy blue')
#sprite color
red=pygame.color('red')
orange=pygame.color('orange')
brown=pygame.color('brown')
black=pygame.color('black')
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color) 
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit=False
        if self.rect.left  <=0 or self.rect.right >=500:
            self.velocity[0]= -self.velocity[0]
            boudary_hit= True 
        if self.rect.top  <=0 or self.rect.right >=400:
            self.velocity[0]= -self.velocity[0]
            boudary_hit= True