import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        
        # velocity 
        velocity_positive = self.velocity.rotate(random_angle) * 1.2
        velocity_negative = self.velocity.rotate(-random_angle) * 1.2 
        
        # new astorids
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity_positive
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity_negative