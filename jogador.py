import pygame
import math
import time
from magica import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.spritesheet_mov = pygame.image.load('Sprites/Personagens/Player/jogador_mov.png').convert_alpha() 
        self.spritesheet_par = pygame.image.load('Sprites/Personagens/Player/jogador_par.png').convert_alpha() 
        self.game = game
        self.x = 100
        self.y = 100
        self.speed = 5
        self.radius = 30
        self.vida = 5
        self.balas = []
        self.taxa_disparo = 0.95
        self.ult_disparo =  time.time()
        self.atirando = False
        self.tamanho = 60
        self.sprite_width = 16
        self.sprite_height = 16
        self.num_frames = 16
        self.direcao_atual = "baixo"
        self.cima_frames = []
        self.baixo_frames = []
        self.esquerda_frames = []
        self.direita_frames = []
        
        #SPRITE DE ANDAR PARA BAIXO
        for row in range(4):  # 4 linhas de frames
            for col in range(4):  # 4 colunas de frames
                if row == 0 and col == 0:
                    # Calculando a posição de cada frame
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    baixo_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    baixo_frame = pygame.transform.scale(baixo_frame, (self.tamanho, self.tamanho))
                    self.baixo_frames.append(baixo_frame)
                elif row == 1 and col == 0:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    baixo_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    baixo_frame = pygame.transform.scale(baixo_frame, (self.tamanho, self.tamanho))
                    self.baixo_frames.append(baixo_frame)
                elif row == 2 and col == 0:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    baixo_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    baixo_frame = pygame.transform.scale(baixo_frame, (self.tamanho, self.tamanho))
                    self.baixo_frames.append(baixo_frame)
                elif row == 3 and col == 0:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    baixo_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    baixo_frame = pygame.transform.scale(baixo_frame, (self.tamanho, self.tamanho))
                    self.baixo_frames.append(baixo_frame)

        #SPRITE DE ANDAR PARA CIMA
        for row in range(4):  # 4 linhas de frames
            for col in range(4):  # 4 colunas de frames
                if row == 0 and col == 1:
                    # Calculando a posição de cada frame
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    cima_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    cima_frame = pygame.transform.scale(cima_frame, (self.tamanho, self.tamanho))
                    self.cima_frames.append(cima_frame)
                elif row == 1 and col == 1:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    cima_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    cima_frame = pygame.transform.scale(cima_frame, (self.tamanho, self.tamanho))
                    self.cima_frames.append(cima_frame)
                elif row == 2 and col == 1:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    cima_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    cima_frame = pygame.transform.scale(cima_frame, (self.tamanho, self.tamanho))
                    self.cima_frames.append(cima_frame)
                elif row == 3 and col == 1:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    cima_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    cima_frame = pygame.transform.scale(cima_frame, (self.tamanho, self.tamanho))
                    self.cima_frames.append(cima_frame)
        
        #SPRITE DE ANDAR PARA ESQUERDA
        for row in range(4):  # 4 linhas de frames
            for col in range(4):  # 4 colunas de frames
                if row == 0 and col == 2:
                    # Calculando a posição de cada frame
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    esquerda_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    esquerda_frame = pygame.transform.scale(esquerda_frame, (self.tamanho, self.tamanho))
                    self.esquerda_frames.append(esquerda_frame)
                elif row == 1 and col == 2:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    esquerda_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    esquerda_frame = pygame.transform.scale(esquerda_frame, (self.tamanho, self.tamanho))
                    self.esquerda_frames.append(esquerda_frame)
                elif row == 2 and col == 2:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    esquerda_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    esquerda_frame = pygame.transform.scale(esquerda_frame, (self.tamanho, self.tamanho))
                    self.esquerda_frames.append(esquerda_frame)
                elif row == 3 and col == 2:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    esquerda_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    esquerda_frame = pygame.transform.scale(esquerda_frame, (self.tamanho, self.tamanho))
                    self.esquerda_frames.append(esquerda_frame)
        
        #SPRITE DE ANDAR PARA DIREITA
        for row in range(4):  # 4 linhas de frames
            for col in range(4):  # 4 colunas de frames
                if row == 0 and col == 3:
                    # Calculando a posição de cada frame
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    direita_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    direita_frame = pygame.transform.scale(direita_frame, (self.tamanho, self.tamanho))
                    self.direita_frames.append(direita_frame)
                elif row == 1 and col == 3:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    direita_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    direita_frame = pygame.transform.scale(direita_frame, (self.tamanho, self.tamanho))
                    self.direita_frames.append(direita_frame)
                elif row == 2 and col == 3:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    direita_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    direita_frame = pygame.transform.scale(direita_frame, (self.tamanho, self.tamanho))
                    self.direita_frames.append(direita_frame)
                elif row == 3 and col == 3:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    direita_frame = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    direita_frame = pygame.transform.scale(direita_frame, (self.tamanho, self.tamanho))
                    self.direita_frames.append(direita_frame)
                    
        self.cima_image = self.cima_frames[0]
        self.baixo_image = self.baixo_frames[0]
        self.esquerda_image = self.esquerda_frames[0]
        self.direita_image = self.direita_frames[0]
        self.rect_cima = self.cima_image.get_rect()   
        self.rect_baixo = self.baixo_image.get_rect()   
        self.rect_esquerda = self.esquerda_image.get_rect()   
        self.rect_direita = self.direita_image.get_rect()   
        # self.rect.topleft = (self.x, self.y)
        
        
        # Criação da varinha mágica
        self.varinha = Varinha(game, self)

        
        
    def update(self, inimigos):

        # Verifica quais teclas estão pressionadas
        keys = pygame.key.get_pressed()
        

        # Movimenta o jogador baseado nas teclas
        if keys[pygame.K_a]:
            self.x -= self.speed
            self.direcao_atual = "esquerda"  # Atualiza a direção para esquerda
            self.rect_esquerda.topleft = (self.x, self.y)
        if keys[pygame.K_d]:
            self.x += self.speed
            self.direcao_atual = "direita"  # Atualiza a direção para direita
            self.rect_direita.topleft = (self.x, self.y)
        if keys[pygame.K_w]:
            self.y -= self.speed
            self.direcao_atual = "cima"  # Atualiza a direção para cima
            self.rect_cima.topleft = (self.x, self.y)
        if keys[pygame.K_s]:
            self.y += self.speed
            self.direcao_atual = "baixo"  # Atualiza a direção para baixo
            self.rect_baixo.topleft = (self.x, self.y)

        
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
        self.balas = [bala for bala in self.balas if 0 < bala.x < 1366 and 0 < bala.y < 768]
        # Permitir disparar novamente se o tempo desde o último disparo for maior que a taxa de disparo
        if time.time() >= self.ult_disparo:
            self.is_shooting = False

    
    def draw(self):
        # pygame.draw.circle(self.game.screen, 'blue', (self.x, self.y), (self.radius))

        if self.direcao_atual == "cima":
            self.game.screen.blit(self.cima_frames[self.game.current_frame // self.game.frame_rate], (self.rect_cima.x, self.rect_cima.y))
        elif self.direcao_atual == "baixo":
            self.game.screen.blit(self.baixo_frames[self.game.current_frame // self.game.frame_rate], (self.rect_baixo.x, self.rect_baixo.y))
        elif self.direcao_atual == "esquerda":
            self.game.screen.blit(self.esquerda_frames[self.game.current_frame // self.game.frame_rate], (self.rect_esquerda.x, self.rect_esquerda.y))
        elif self.direcao_atual == "direita":
            self.game.screen.blit(self.direita_frames[self.game.current_frame // self.game.frame_rate], (self.rect_direita.x, self.rect_direita.y))
        
        # Desenha a varinha
        self.varinha.draw()
        
        # Desenha as balas
        for bala in self.balas:
            bala.draw()

    def shoot(self):
        # Verifica se o tempo desde o último disparo é maior ou igual à taxa de disparo

        if time.time() >= self.ult_disparo and not self.atirando:
            self.atirando = True
            # Atualiza o tempo do último disparo
            self.ult_disparo = time.time() + self.taxa_disparo
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