import pygame
import circleshape.py import CircleShape
from constants import *


def main():
    pygame.init()

    # Create a display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    clock = pygame.time.Clock()
    dt = 0
    test_ciricle = CircleShape(100, 100, 20)
    
    # Main game loop
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

        screen.fill("Black")
        pygame.display.flip()

        # cap the frame
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    print("Starting asteroids!")
    main()
