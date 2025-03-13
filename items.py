import pygame
import random
import math


class Item:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.radius = 20
        self.tamanho = 35


    def acerto_jogador(self, jogador):

        distance = math.sqrt((self.x - jogador.x) ** 2 + (self.y - jogador.y) ** 2)
        return distance <= self.tamanho + jogador.radius

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(
            self.game.screen, 'red', (int(self.x), int(self.y)), self.radius
        )
