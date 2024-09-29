import pygame

class Dificuldade:
    def __init__(self, game, inimigos):
        self.game = game
        self.inimigos = inimigos

    def subindo_dificuldade(self):
        if self.game.pontos >= 9900:
            self.game.num_inimigos = 5 
        elif 5900 <= self.game.pontos < 9900:
            self.game.num_inimigos = 4
            # self.game.inimigo_speed = 4
        elif 2900 <= self.game.pontos < 5900:
            self.game.num_inimigos = 3
        elif 1400 <= self.game.pontos < 2900:
            self.game.inimigo_speed = 3