import pygame

_ = False
map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]

class Map:
    def __init__(self, game):
        self.game = game
        self.map = map
        self.world_map = {}
        self.get_map()
    
    def get_map(self):
        for j, linha in enumerate(self.map):
            for i, valor in enumerate(linha):
                if valor:
                    self.world_map[(i, j)] = valor
                    
    def draw(self):
        [pygame.draw.rect(self.game.screen, 'green', (pos[0] * 50, pos[1] * 50, 50, 50), 2)
         for pos in self.world_map]