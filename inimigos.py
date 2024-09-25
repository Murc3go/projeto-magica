import pygame
import random


class Inimigo:
    def __init__(self, game):
        self.game = game
        self.x = random.randint(10, self.game.screen.get_width() - 10)
        self.y = random.randint(10, self.game.screen.get_height() - 10)
        self.speed = 2
        self.radius = 10
        
    def update(self):
        
        self.x -= self.speed
        
        # Mantém o inimigo dentro da tela
        if self.x - self.radius < 0:
            self.x = self.radius
        elif self.x + self.radius > self.game.screen.get_width():
            self.x = self.game.screen.get_width() - self.radius
        if self.y - self.radius < 0:
            self.y = self.radius
        elif self.y + self.radius > self.game.screen.get_height():
            self.y = self.game.screen.get_height() - self.radius
    
    def draw(self):
        pygame.draw.circle(self.game.screen, 'red', (self.x, self.y), (self.radius))