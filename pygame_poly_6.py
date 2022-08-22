import pygame

pygame.init()
screen = pygame.display.set_mode((400,400))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.polygon(screen, (125,255,45), ((23,65),(87,21),(54,65),(87,98)),width=5)
    pygame.display.flip()
