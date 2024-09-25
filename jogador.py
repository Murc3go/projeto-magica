import pygame
import math
import time
from mapa import *
from magica import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x = 100
        self.y = 100
        self.speed = 5
        self.radius = 20
        self.balas = []
        self.taxa_disparo = 1
        self.ult_disparo =  - self.taxa_disparo
        
        # Criação da varinha mágica
        self.varinha = Varinha(game, self, 40)  # A varinha gira a 40px de distância do player
        
    def update(self):

        # Verifica quais teclas estão pressionadas
        keys = pygame.key.get_pressed()
        
        # Movimenta o jogador baseado nas teclas
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
            
        # Mantém o player dentro da tela
        if self.x - self.radius < 0:
            self.x = self.radius
        elif self.x + self.radius > self.game.screen.get_width():
            self.x = self.game.screen.get_width() - self.radius
        if self.y - self.radius < 0:
            self.y = self.radius
        elif self.y + self.radius > self.game.screen.get_height():
            self.y = self.game.screen.get_height() - self.radius
            
        # Atualização da varinha
        self.varinha.update()
        
        for bala in self.balas:
            bala.update()
        # Remove balas que saíram da tela
        self.balas = [bala for bala in self.balas if 0 < bala.x < 800 and 0 < bala.y < 600]

    
    def draw(self):
        pygame.draw.circle(self.game.screen, 'blue', (self.x, self.y), (self.radius))
        
        # Desenha a varinha
        self.varinha.draw()
        
        # Desenha as balas
        for bala in self.balas:
            bala.draw()

    def shoot(self):
        # Verifica se o tempo desde o último disparo é maior ou igual à taxa de disparo
        tempo_atual = time.time()

        if tempo_atual - self.ult_disparo >= self.taxa_disparo:
            # Atualiza o tempo do último disparo
            self.ult_disparo = tempo_atual
            # Obter a posição do mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
        
            # Calcular a diferença entre a posição do mouse e da varinha
            dx = mouse_x - self.varinha.x
            dy = mouse_y - self.varinha.y
        
            # Normalizar o vetor de direção
            distance = math.sqrt(dx**2 + dy**2)
            direction_x = dx / distance
            direction_y = dy / distance
        
            # Cria uma nova bala na posição do player
            nova_bala = Balas(self.game, self.varinha.x, self.varinha.y, direction_x, direction_y)
            self.balas.append(nova_bala)