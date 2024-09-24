import sys
import pygame
import player
import asteroid
import asteroidfield
import shot
from constants import *


def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable) 
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, updatable, drawable)


    player_instance = player.Player(x, y)
    asteroidfield_instance = asteroidfield.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(SCREEN_COLOR)

        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)
            
        for obj in asteroids:
            if(obj.has_collided(player_instance)):
                print("Game over!")
                sys.exit()
            
            for bullet in shots:
                if (obj.has_collided(bullet)):
                    obj.split()
                    bullet.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()