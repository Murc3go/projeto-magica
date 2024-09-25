import pygame
import math
import time
from tela import *
from magica import *
from inimigos import *


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

    def checar_colisao(self, mov_x, mov_y):
        # Calcula a célula do mapa com base nas coordenadas do jogador
        grid_x = int(mov_x // 51.2)
        grid_y = int(mov_y // 51.25)

        # Verifica se a célula é uma parede (1 no mapa)
        if (grid_x, grid_y) in self.game.map.world_map:
            return True
        return False

        
        
    def update(self):

        # Verifica quais teclas estão pressionadas
        keys = pygame.key.get_pressed()
        
        mov_x, mov_y = self.x, self.y

        # Movimenta o jogador baseado nas teclas
        if keys[pygame.K_a]:
            mov_x -= self.speed
        if keys[pygame.K_d]:
            mov_x += self.speed
        if keys[pygame.K_w]:
            mov_y -= self.speed
        if keys[pygame.K_s]:
            mov_y += self.speed

        # Verifica a colisão antes de permitir o movimento
        if not self.checar_colisao(mov_x, self.y):
            self.x = mov_x
        if not self.checar_colisao(self.x, mov_y):
            self.y = mov_y

            
        # Atualização da varinha
        self.varinha.update()
        
        for bala in self.balas:
            bala.update(self.game.inimigos, self.game.pontos)
        # Remove balas que saíram da tela
        self.balas = [bala for bala in self.balas if 0 < bala.x < 1280 and 0 < bala.y < 720]

    
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