# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import * 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x,y)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__=="__main__":
    main()
