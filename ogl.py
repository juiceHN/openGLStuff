import pygame
import random as rr
WHITE = (255, 255, 255)
pygame.init()
window = pygame.display.set_mode((800, 800))
done = False
x, y = 50, 50
while not done:
    r = rr.randint(0, 255)
    g = rr.randint(0, 255)
    b = rr.randint(0, 255)
    color = (r, g, b)
    pygame.draw.rect(window, color, [x, y, 50, 50], 5)
    pygame.display.flip()
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            x += 10
        if pressed[pygame.K_LEFT]:
            x = x - 10
        if pressed[pygame.K_DOWN]:
            y = y + 10
        if pressed[pygame.K_UP]:
            y = y - 10
