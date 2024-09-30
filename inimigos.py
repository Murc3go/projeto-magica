import pygame
import random
import math
from spritesheet import Spritesheet


class Inimigo(pygame.sprite.Sprite):
    def __init__(self, game, inimigo_speed):
        pygame.sprite.Sprite.__init__(self)
        self.spritesheet = pygame.image.load('Sprites/Personagens/Skull.png').convert_alpha()
        self.width = 16
        self.height = 16
        
        # Criando uma superfície para a imagem do inimigo
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(self.spritesheet, (0, 0), (0, 0, self.width, self.height))  # Carrega uma parte do spritesheet
        # pygame.transform.scale(pygame.image.load('Sprites/Painel/painel3.png'), (self.tile_size, self.tile_size))
        # Define o retângulo do sprite
        self.rect = self.image.get_rect()
        
        self.game = game
        self.x, self.y = self.spawn_posicao()
        self.speed = inimigo_speed
        self.radius = 20
        self.vida = True
        self.rect.topleft = (self.x, self.y)

    def spawn_posicao(self):
        while True:
            # Gera coordenadas aleatórias
            x = random.randint(10, self.game.screen.get_width() - 10)
            y = random.randint(10, self.game.screen.get_height() - 10)

            # Converte as coordenadas para as células do grid
            grid_x = int(x // 55)
            grid_y = int(y // 55)

            # Verifica se a posição no mapa não é uma barreira (células com 1)
            if (grid_x, grid_y) not in self.game.map.map_layout:
                
                # Verifica a distância do jogador
                jogador_dx = x - self.game.player.x
                jogador_dy = y - self.game.player.y
                distance_to_player = math.sqrt(jogador_dx ** 2 + jogador_dy ** 2)

                # Verifica se a distância é maior que um limite (150 pixels)
                if distance_to_player >= 150:
                    return x, y
        
    def acerto_bala(self, bala):
        # Verifica se a distância entre o centro da bala e o inimigo é menor ou igual à soma dos raios
        distance = math.sqrt((self.x - bala.x) ** 2 + (self.y - bala.y) ** 2)
        return distance <= self.radius + bala.radius
    
    def acerto_jogador(self, jogador):
        # Verifica se a distância entre o centro do jogodor e o inimigo é menor ou igual à soma dos raios
        distance = math.sqrt((self.x - jogador.x) ** 2 + (self.y - jogador.y) ** 2)
        return distance <= self.radius + jogador.radius
    
    def update(self, jogador):
       if self.vida:
            # Calcula a direção do player
            dx = jogador.x - self.x
            dy = jogador.y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            # Normaliza o vetor de direção
            if distance != 0:
                dx /= distance
                dy /= distance

            # Move o inimigo na direção do player
            self.x += dx * self.speed
            self.y += dy * self.speed
            
            self.rect.topleft = (self.x, self.y)

    
    def draw(self):
        if self.vida:
            # pygame.draw.circle(self.game.screen, 'red', (self.x, self.y), (self.radius))
            self.game.screen.blit(self.image, (self.rect.x, self.rect.y)) 