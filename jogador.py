import pygame
import math
from tela import *
from magica import *
from inimigos import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.x = 100
        self.y = 100
        self.speed = 5
        self.radius = 40
        self.vida = 5
        self.balas = []
        self.taxa_disparo = 100
        self.ult_disparo =  - self.taxa_disparo
        
        
        # Criação da varinha mágica
        self.varinha = Varinha(game, self, 40)  # A varinha gira a 40px de distância do player

        
        
    def update(self, inimigos):

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

        
        inimigos_a_remover = []
        for inimigo in inimigos:
            if inimigo.vida and inimigo.acerto_jogador(self):
                inimigos_a_remover.append(inimigo)
                self.vida -= 1

        for inimigo in inimigos_a_remover:
            inimigos.remove(inimigo)
            
        # Atualização da varinha
        self.varinha.update()
        
        for bala in self.balas:
            bala.update(self.game.inimigos)
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

        if pygame.time.get_ticks() >= self.ult_disparo:
            # Atualiza o tempo do último disparo
            self.ult_disparo += self.taxa_disparo
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