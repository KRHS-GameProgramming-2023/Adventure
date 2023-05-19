import pygame, sys,math,random
from player import *

pygame.init()


clock = pygame.time.Clock()

size = [900, 700]
screen = pygame.display.set_mode([900, 700])

player=Player(5,[900/2,700/2])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
        elif event.type==pygame.KEYDOWN:          
            if event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_LEFT:
                player.go("left")
        elif event.type==pygame.KEYUP:        
            if event.key == pygame.K_RIGHT:
                player.go("sright")
            if event.key == pygame.K_LEFT:
                player.go("sleft")
        
    player.move()
    
    screen.fill((53, 136, 121))
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(80)
    
