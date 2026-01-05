# this allows us to use code from
# the open-source pygame library
# throughout this file
# import os
# os.environ["SDL_VIDEODRIVER"]="x12"
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fpsclock = pygame.time.Clock()
    dt = 0

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Game Over!', True, (0, 255, 0), (0, 0, 128))
    textRect = text.get_rect()
    textRect.center = (400 // 2, 400 // 2)

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        for item in updatable:
            item.update(dt)

        for item in asteroids:
            if item.crash(player):
                print("Game over!")
                screen.blit(text, textRect)
                pygame.time.wait(1500)
                pygame.quit()

            for shot in shots:
                if item.crash(shot):
                    shot.kill()
                    item.split()
                

        for item in drawable:
            item.draw(screen)


        pygame.display.flip()
        dt = fpsclock.tick(60)/1000


if __name__ == "__main__":
    main()
