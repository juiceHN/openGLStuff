import pygame
import random as rr
WHITE = (255, 255, 255)
pygame.init()
window = pygame.display.set_mode((800, 800))
done = False
x, y = 50, 50
while not done:
	pygame.draw.line(screen, WHITE, (10, 10), (500, 500))
	pygame.draw.line(screen, WHITE, (500, 500), 30, 1)
    window.set_at((x, y), color)
    pygame.display.flip()
    window.fill((0,0,0))
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		done = True
    	pressed = pygame.key.get_pressed()
    	if pressed[pygame.K_RIGHT]:
    		x += 10
    	if pressed[pygame.K_LEFT]:
    		x = x - 10
    	if pressed[pygame.K_DOWN]:
    		y = y - 10
    	if pressed[pygame.K_UP]:
    		y = y + 10

