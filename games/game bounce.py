import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT=pygame.USEREVENT+1
BACKGROUND_COLOR_CHANGE_EVENT=pygame.USEREVENT+2
#background colors
blue=pygame.Color('blue')
yellow=pygame.Color('navy blue')
navy_blue=pygame.Color('light blue')
#sprite color
red=pygame.Color('red')
orange=pygame.Color('orange')
brown=pygame.Color('brown')
black=pygame.Color('yellow')
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
            self.velocity[1]= -self.velocity[1]
            boundary_hit= True 
        if self.rect.top  <=0 or self.rect.bottom >=400:
            self.velocity[1]= -self.velocity[1]
            boundary_hit= True
        if  boundary_hit :
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    def change_color(self):
        self.image.fill(random.choice([red,orange,brown,black]))   
def change_background_color():
    global bgcolor
    bgcolor=random.choice([blue,yellow,navy_blue])
all_sprite_list=pygame.sprite.Group()
sp1=Sprite(red,20,30)
sp1.rect.x = random.randint(0, 480)

sp1.rect.y = random.randint(0, 370)
all_sprite_list.add(sp1)  
screen = pygame.display.set_mode((500, 400))

pygame.display.set_caption("Colorful Bounce")

bgcolor = blue

screen.fill(bgcolor)

exit = False

clock = pygame.time.Clock()
while not exit:

    for event in pygame.event.get():

# If the window's close button is clicked, exit the game

        if event.type == pygame.QUIT:

            exit = True

# If the sprite color change event is triggered, change the sprite's color

        elif event.type == SPRITE_COLOR_CHANGE_EVENT:

            sp1.change_color()

# If the background color change event is triggered, change the background color

        
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()
# Update all sprites

            all_sprite_list.update()

# Fill the screen with the current background color

screen.fill(bgcolor)

# Draw all sprites to the screen

all_sprite_list.draw(screen)

# Refresh the display

pygame.display.flip()

# Limit the frame rate to 240 fps

clock.tick(60)

# Uninitialize all pygame modules and close the window

pygame.quit()              