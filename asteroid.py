import random
import circleshape
import pygame
from constants import *

class Asteroid(circleshape.CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, ASTEROID_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_radius = self.radius - ASTEROID_MIN_RADIUS

        split_angle = random.uniform(20, 60)
        a1_direction = self.velocity.rotate(split_angle)
        a2_direction = self.velocity.rotate(-split_angle)

        a1 = Asteroid(self.position.x, self.position.y, split_radius)
        a2 = Asteroid(self.position.x, self.position.y, split_radius)

        a1.velocity = a1_direction * ASTEROID_SPLIT_SPEED_MULTIPLIER
        a2.velocity = a2_direction * ASTEROID_SPLIT_SPEED_MULTIPLIER
