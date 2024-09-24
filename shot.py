import circleshape
import pygame
from constants import *


class Shot(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, SHOT_COLOR, self.position, self.radius, SHOT_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)