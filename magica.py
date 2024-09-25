import pygame
import math
from inimigos import *


class Varinha:
    def __init__(self, game, player, radius):
        self.game = game
        self.player = player # A referência ao jogador
        self.radius = radius # Distância do centro do player
    
    def update(self):
        # Obter a posição do mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Calcular a direção do mouse em relação ao jogador
        dx = mouse_x - self.player.x
        dy = mouse_y - self.player.y

        # Normalizar o vetor de direção (fazer o vetor ter comprimento 1)
        distance = math.sqrt(dx**2 + dy**2)
        if distance != 0:  # Evitar divisão por zero
            direction_x = dx / distance
            direction_y = dy / distance
        else:
            direction_x = 0
            direction_y = 0
        
        # Posicionar a varinha a uma distância fixa (self.radius) ao redor do jogador
        self.x = self.player.x + direction_x * self.radius
        self.y = self.player.y + direction_y * self.radius
    
    def draw(self):
       # Desenhar a varinha na posição calculada
        pygame.draw.circle(self.game.screen, 'brown', (int(self.x), int(self.y)), 10)  # Ajustar o tamanho da varinha
        
        
class Balas:
    def __init__(self, game, x , y, direction_x, direction_y):
        self.game = game
        self.x = x
        self.y = y
        self.speed = 10
        self.radius = 5
        self.direction_x = direction_x
        self.direction_y = direction_y
        
    def update(self, inimigos, game):
        self.y += self.direction_y * self.speed
        self.x += self.direction_x * self.speed
    
        # Verifica se colidiu com algum inimigo
        for inimigo in inimigos:
            if inimigo.vida and inimigo.acerto_bala(self):
                inimigo.vida = False            # Remove o inimigo ao colidir
                inimigos.remove(inimigo)        # Remove o inimigo do array
                
                self.game.pontos += 100

    
    def draw(self):
        pygame.draw.circle(self.game.screen, 'white', (self.x, self.y), (self.radius))