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
        self.projetil = []
        self.taxa_disparo = 0.75
        self.ult_disparo =  - self.taxa_disparo
        self.atirando = False
        self.tamanho = 40
        self.sprite_width = 16
        self.sprite_height = 16
        self.direcao_atual = "baixo"
        self.movimentacao = False
        self.cima_frames = []
        self.baixo_frames = []
        self.esquerda_frames = []
        self.direita_frames = []
        self.parado_baixo = None
        self.parado_cima = None
        self.parado_esquerda = None
        self.parado_direita = None
        
        
        #SPRITE PARADO
        for row in range(1):  # 0 linhas de frames
            for col in range(4):  # 4 colunas de frames
                if row == 0 and col == 0:
                    # Calculando a posição de cada frame
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    self.parado_baixo = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    self.parado_baixo = pygame.transform.scale(self.parado_baixo, (self.tamanho, self.tamanho))
                elif row == 0 and col == 1:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    self.parado_cima = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    self.parado_cima = pygame.transform.scale(self.parado_cima, (self.tamanho, self.tamanho))
                elif row == 0 and col == 2:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    self.parado_esquerda = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    self.parado_esquerda = pygame.transform.scale(self.parado_esquerda, (self.tamanho, self.tamanho))
                elif row == 0 and col == 3:
                    frame_x = col * self.sprite_width
                    frame_y = row * self.sprite_height
                    self.parado_direita = self.spritesheet_mov.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
                    self.parado_direita = pygame.transform.scale(self.parado_direita, (self.tamanho, self.tamanho))
        
        self.par_cima_img = self.parado_cima
        self.par_baixo_img = self.parado_baixo
        self.par_esq_img = self.parado_esquerda
        self.par_dir_img = self.parado_direita 
        if self.par_cima_img:
            self.rect_par_cima = self.par_cima_img.get_rect()
        if self.par_baixo_img:
            self.rect_par_baixo = self.par_baixo_img.get_rect()
        if self.par_esq_img:
            self.rect_par_esq = self.par_esq_img.get_rect()
        if self.par_dir_img:
            self.rect_par_dir = self.par_dir_img.get_rect()    
                    
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
    
    def update_direction(self):
        # Pega a posição do mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Calcula o centro do jogador
        centro_x = self.x + self.tamanho // 2
        centro_y = self.y + self.tamanho // 2

        # Calcula a diferença entre o mouse e o jogador
        delta_x = mouse_x - centro_x
        delta_y = mouse_y - centro_y

        # Calcula o ângulo em radianos
        angulo = math.atan2(delta_y, delta_x)

        # Converte o ângulo de radianos para graus
        angulo_graus = math.degrees(angulo)

        # Determina a direção com base no ângulo
        if -45 <= angulo_graus < 45:
            self.direcao_atual = "direita"
            self.rect_direita.topleft = (self.x, self.y)
        elif 45 <= angulo_graus < 135:
            self.direcao_atual = "baixo"
            self.rect_baixo.topleft = (self.x, self.y)
        elif -135 <= angulo_graus < -45:
            self.direcao_atual = "cima"
            self.rect_cima.topleft = (self.x, self.y)
        else:
            self.direcao_atual = "esquerda"
            self.rect_esquerda.topleft = (self.x, self.y)   

        
        
    def update(self, inimigos):
        
        self.update_direction()
            
        self.movimentacao = False

        # Verifica quais teclas estão pressionadas
        keys = pygame.key.get_pressed()

        # Movimenta o jogador baseado nas teclas
        if keys[pygame.K_a]:
            self.x -= self.speed
            self.movimentacao = True
        if keys[pygame.K_d]:
            self.x += self.speed
            self.movimentacao = True
        if keys[pygame.K_w]:
            self.y -= self.speed
            self.movimentacao = True
        if keys[pygame.K_s]:
            self.y += self.speed
            self.movimentacao = True

        # Atualiza a posição do sprite de parado quando não está se movendo
        if not self.movimentacao:
            if self.direcao_atual == "esquerda":
                self.rect_par_esq.topleft = (self.x, self.y)
            elif self.direcao_atual == "direita":
                self.rect_par_dir.topleft = (self.x, self.y)
            elif self.direcao_atual == "cima":
                self.rect_par_cima.topleft = (self.x, self.y)
            elif self.direcao_atual == "baixo":
                self.rect_par_baixo.topleft = (self.x, self.y)

        
        inimigos_a_remover = []
        for inimigo in inimigos:
            if inimigo.vida and inimigo.acerto_jogador(self):
                inimigos_a_remover.append(inimigo)
                self.vida -= 1

        for inimigo in inimigos_a_remover:
            inimigos.remove(inimigo)
                    
        
        for projetil in self.projetil:
            projetil.update(self.game.inimigos)
            
        # Remove balas que saíram da tela
        self.projetil = [projetil for projetil in self.projetil if 0 < projetil.x < 1366 and 0 < projetil.y < 768]
        

    
    def draw(self):
        # pygame.draw.circle(self.game.screen, 'blue', (self.x, self.y), (self.radius))
        
        # Renderiza o sprite parado dependendo da direção
        if self.movimentacao:
            if self.direcao_atual == "cima":
                self.game.screen.blit(self.cima_frames[self.game.current_frame // self.game.frame_rate], (self.rect_cima.x, self.rect_cima.y))
            elif self.direcao_atual == "baixo":
                self.game.screen.blit(self.baixo_frames[self.game.current_frame // self.game.frame_rate], (self.rect_baixo.x, self.rect_baixo.y))
            elif self.direcao_atual == "esquerda":
                self.game.screen.blit(self.esquerda_frames[self.game.current_frame // self.game.frame_rate], (self.rect_esquerda.x, self.rect_esquerda.y))
            elif self.direcao_atual == "direita":
                self.game.screen.blit(self.direita_frames[self.game.current_frame // self.game.frame_rate], (self.rect_direita.x, self.rect_direita.y))
        else:
            
            if self.direcao_atual == "cima":
                self.game.screen.blit(self.parado_cima, (self.rect_par_cima.x, self.rect_par_cima.y))
            elif self.direcao_atual == "baixo":
                self.game.screen.blit(self.parado_baixo, (self.rect_par_baixo.x, self.rect_par_baixo.y))
            elif self.direcao_atual == "esquerda":
                self.game.screen.blit(self.parado_esquerda, (self.rect_par_esq.x, self.rect_par_esq.y))
            elif self.direcao_atual == "direita":
                self.game.screen.blit(self.parado_direita, (self.rect_par_dir.x, self.rect_par_dir.y))
                
        for projetil in self.projetil:
            
            projetil.draw()

    def shoot(self):
        agora = time.time()
        
        if agora - self.ult_disparo >= self.taxa_disparo:
            # self.aura_start = True
            self.ult_disparo = agora  # Atualiza o último disparo
        
        
            # Obtém a posição atual do mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            
            # Calcula o centro do player
            self.centro_x = self.x + self.tamanho // 2
            self.centro_y = self.y + self.tamanho // 2

            # Cria um novo projétil na posição do player que vai em direção ao mouse
            novo_projetil = Magica(self.game, self.centro_x, self.centro_y, mouse_x, mouse_y)
            self.projetil.append(novo_projetil)
            
    
            