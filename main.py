import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_object = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = (updatable)

    Asteroid.containers = (asteroids, updatable, drawable)

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black')

        

        updatable.update(dt)


            

        for object in asteroids:
            
            for shot in shots:
                if shot.collides_with(object):
                    shot.kill()
                    object.split()
                    

            if object.collides_with(player):
                print("Game over!")
                sys.exit()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        dt = clock_object.tick(60) / 1000
        


if __name__ == "__main__":
    main()
