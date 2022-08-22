import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.ellipse(screen, (125,255,45), [255,60,500,250],2)
    pygame.display.flip()
