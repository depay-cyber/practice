import pygame

import random

pygame.init()

# Custom events for sprite and background color changes

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1

BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Background colors

blue = pygame.Color('blue')

yellow = pygame.Color('yellow')

navy_blue = pygame.Color('navy')

# Sprite colors

red = pygame.Color('red')

orange = pygame.Color('orange')

brown = pygame.Color('brown')

black = pygame.Color('black')

class Sprite(pygame.sprite.Sprite):

def __init__(self, color, height, width):

super().__init__()

self.image = pygame.Surface([width, height])

self.image.fill(color)

self.rect = self.image.get_rect()

self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

def update(self):

# Move the sprite

self.rect.move_ip(self.velocity)

boundary_hit = False

# Check for collisions with the window edges

if self.rect.left <= 0 or self.rect.right >= 500:

self.velocity[0] = -self.velocity[0]

boundary_hit = True

if self.rect.top <= 0 or self.rect.bottom >= 400:

self.velocity[1] = -self.velocity[1]

boundary_hit = True

# If the sprite hits a boundary, post events to change colors

if boundary_hit:

pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))

pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

def change_color(self):

# Change the color of the sprite to a random choice

self.image.fill(random.choice([red, orange, brown, black]))

def change_background_color():

# Change the global background color to a random choice

global bg_color

bg_color = random.choice([blue, yellow, navy_blue])

# Initialize the sprite group and create a sprite

all_sprite_list = pygame.sprite.Group()

sp1 = Sprite(red, 20, 30)

sp1.rect.x = random.randint(0, 480)

sp1.rect.y = random.randint(0, 370)

all_sprite_list.add(sp1)

# Set up the display

screen = pygame.display.set_mode((500, 400))

pygame.display.set_caption("Colorful Bounce")

# Initialize background color

bg_color = blue

screen.fill(bg_color)

# Game loop variables

exit_game = False

clock = pygame.time.Clock()

# Main game loop

while not exit_game:

    for event in pygame.event.get():

# Handle window close

        if event.type == pygame.QUIT:

            exit_game = True

# Handle sprite color change event

        elif event.type == SPRITE_COLOR_CHANGE_EVENT:

            sp1.change_color()

# Handle background color change event
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:

            change_background_color()

# Update all sprites

all_sprite_list.update()

# Fill the screen with the current background color

screen.fill(bg_color)

# Draw all sprites to the screen

all_sprite_list.draw(screen)

# Refresh the display

pygame.display.flip()

# Limit the frame rate to 60 FPS

clock.tick(60)

# Quit pygame

pygame.quit()