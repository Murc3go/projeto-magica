import pygame
import math

        
class Magica:
    def __init__(self, game, x, y, target_x, target_y):
        self.game = game
        self.x = x
        self.y = y
        self.speed = 15
        self.radius = 5
        
        # Calcula a direção do projétil baseado na posição do mouse (target_x, target_y)
        direction_x = target_x - self.x
        direction_y = target_y - self.y
        distance = math.sqrt(direction_x**2 + direction_y**2)  # Distância até o alvo
        self.direction_x = direction_x / distance  # Normalizando a direção
        self.direction_y = direction_y / distance  # Normalizando a direção
        
    def update(self, inimigos):
        # Mover o projétil na direção calculada
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed
    
        # Verifica se colidiu com algum inimigo
        for inimigo in inimigos:
            if inimigo.vida and inimigo.acerto_bala(self):
                inimigo.vida = False            # Remove o inimigo ao colidir
                inimigos.remove(inimigo)        # Remove o inimigo do array
                
                self.game.pontos += 100

    
    def draw(self):
        pygame.draw.circle(self.game.screen, 'white', (self.x, self.y), (self.radius))