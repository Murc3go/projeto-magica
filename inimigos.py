import pygame
import random


class Inimigo:
    def __init__(self, game):
        self.game = game
        self.x = random.randint(10, self.game.screen.get_width() - 10)
        self.y = random.randint(10, self.game.screen.get_height() - 10)
        self.speed = 2
        self.radius = 10
    
    def draw(self):
        pygame.draw.circle(self.game.screen, 'red', (self.x, self.y), (self.radius))