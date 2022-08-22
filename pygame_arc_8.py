import pygame
from math import pi
pygame.init()
screen = pygame.display.set_mode((400,400))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.arc(screen, (125, 255, 45), [210, 75, 150, 125], 0, pi / 2, 2) 
    pygame.display.flip()
