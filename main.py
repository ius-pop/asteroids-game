# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import * 
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
   

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # Add player to sprite groups
    Player.containers = (updatable, drawable)

    #create a sprite group for asteroids
    asteroids = pygame.sprite.Group()
    #add asteroids to sprite groups
    Asteroid.containers = (asteroids,updatable, drawable)

    #create player
    player = Player(x,y)

    AsteroidField.containers = updatable
    asterroidfield = AsteroidField(player)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        #check for collisions
        for a in asteroids:
            if player.collision(a):
                print("Game Over!")
                return

        screen.fill((0,0,0))
        
        for el in drawable: 
            el.draw(screen)
     
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__=="__main__":
    main()
