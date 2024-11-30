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
        # Use the screen's fill method to fill the screen with a solid "black" color
        screen.fill((0, 0, 0))

        # Use pygame's display.flip() method to refresh the screen. Be sure to call this last!
        pygame.display.flip()


if __name__ == "__main__":
    print("Starting asteroids!")
    main()
