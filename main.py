from constants import *
import pygame


def main():
    # Initialize
    pygame.init()

    # Create a display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("Black")
        pygame.display.flip()


if __name__ == "__main__":
    print("Starting asteroids!")
    main()
