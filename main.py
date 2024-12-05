import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField

def main():
    pygame.init()

    # Create a display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    
    clock = pygame.time.Clock()
    dt = 0
    
    #create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    # Player class to groups
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    
    # Initialize the player and add it to groups
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update all objects in the updatable group
        for obj in updatable:
            obj.update(dt)
            
        # Collision detection
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over")
                return pygame.quit()
        
        # Draw all objects in the drawable group        
        screen.fill("Black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # cap the frame
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    print("Starting asteroids!")
    main()
