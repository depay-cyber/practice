import pygame
pygame.init()
#screen
screen=pygame.display.set_mode((400,500))
screen.fill((67,46,9))

done=False
while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
        pygame.draw.rect(screen,(24,99,147),pygame.Rect(30,30,60,60))    
    pygame.display.flip()
            

