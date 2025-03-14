import pygame
import math
from settings import *
from items import *

        
class Magica(pygame.sprite.Sprite):
    def __init__(self, game, x, y, target_x, target_y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = self.game.screen
        self.x = x
        self.y = y
        self.speed = 15
        self.radius = 5
        self.tamanho = 60
        self.remover = False
        direction_x = target_x - self.x
        direction_y = target_y - self.y
        distance = math.sqrt(direction_x**2 + direction_y**2)  # Distância até o alvo
        self.direction_x = direction_x / distance  # Normalizando a direção
        self.direction_y = direction_y / distance  # Normalizando a direção
        
    def update(self, inimigos, itens, projetil):
        # Mover o projétil na direção calculada
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed
    
        # Verifica se colidiu com algum inimigo
        for inimigo in inimigos:
            if inimigo.vida and inimigo.acerto_bala(self):
                inimigo.vida = False
                inimigos.remove(inimigo)        
                self.game.pontos += 100
                item = ItemMoeda(self,self.x, self.y, "Sprites/Itens/moeda.png")
                itens.append(item)
                self.game.animation_itens.add(item)
                self.remover = True

        projetil[:] = [p for p in projetil if not p.remover]
    
    def draw(self):
        pygame.draw.circle(self.game.screen, 'white', (self.x, self.y), (self.radius))

        