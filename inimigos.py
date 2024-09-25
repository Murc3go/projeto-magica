import pygame
import random
import math
from tela import *
from magica import *


class Inimigo:
    def __init__(self, game):
        self.game = game
        self.x = random.randint(10, self.game.screen.get_width() - 10)
        self.y = random.randint(10, self.game.screen.get_height() - 10)
        self.speed = 2
        self.radius = 20
        self.vida = True
        
        
    def collision(self, bala):
        # Verifica se a distância entre o centro da bala e o inimigo é menor ou igual à soma dos raios
        distance = math.sqrt((self.x - bala.x) ** 2 + (self.y - bala.y) ** 2)
        return distance <= self.radius + bala.radius
    def update(self):
        pass
    
    def draw(self):
        if self.vida:
            pygame.draw.circle(self.game.screen, 'red', (self.x, self.y), (self.radius))