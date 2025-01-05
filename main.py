# this allows us to use code from
# the open-source pygame library
# throughout this file
# import os
# os.environ["SDL_VIDEODRIVER"]="x12"
import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fpsclock = pygame.time.Clock()
    dt = 0

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)


        pygame.display.flip()
        dt = fpsclock.tick(60)/1000


if __name__ == "__main__":
    main()
