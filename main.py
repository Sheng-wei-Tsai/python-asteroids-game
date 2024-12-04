import pygame
from circleshape import CircleShape
from constants import *
from player import Player



def main():
    pygame.init()

    # Create a display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    dt = 0
    
    # Main game loop
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
        #
        player.update(dt)
        
        screen.fill("Black")
        player.draw(screen)
        pygame.display.flip()

        # cap the frame
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    print("Starting asteroids!")
    main()
