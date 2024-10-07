import pygame
import math

        
class Magica(pygame.sprite.Sprite):
    def __init__(self, game, x, y, target_x, target_y):
        pygame.sprite.Sprite.__init__(self)
        # self.spritesheet_magica= pygame.image.load('Sprites/FX/EnergyBall.png').convert_alpha() 
        self.game = game
        self.x = x
        self.y = y
        self.speed = 15
        self.radius = 5
        self.tamanho = 60
        # self.sprite_width = 16
        # self.sprite_height = 16
        # self.magica_frames = []
        
        # Calcula a direção do projétil baseado na posição do mouse (target_x, target_y)
        direction_x = target_x - self.x
        direction_y = target_y - self.y
        distance = math.sqrt(direction_x**2 + direction_y**2)  # Distância até o alvo
        self.direction_x = direction_x / distance  # Normalizando a direção
        self.direction_y = direction_y / distance  # Normalizando a direção

        # #SPRITE AURA
        # for row in range(1):  # 0 linhas de frames
        #     for col in range(4):  # 4 colunas de frames
        #         if row == 0 and col == 0:
        #             # Calculando a posição de cada frame
        #             frame_x = col * self.sprite_width
        #             frame_y = row * self.sprite_height
        #             magica_frame = self.spritesheet_magica.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
        #             magica_frame = pygame.transform.scale(magica_frame, (self.tamanho, self.tamanho))
        #             self.magica_frames.append(magica_frame)
        #         elif row == 0 and col == 1:
        #             frame_x = col * self.sprite_width
        #             frame_y = row * self.sprite_height
        #             magica_frame = self.spritesheet_magica.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
        #             magica_frame = pygame.transform.scale(magica_frame, (self.tamanho, self.tamanho))
        #             self.magica_frames.append(magica_frame)
        #         elif row == 0 and col == 2:
        #             frame_x = col * self.sprite_width
        #             frame_y = row * self.sprite_height
        #             magica_frame = self.spritesheet_magica.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
        #             magica_frame = pygame.transform.scale(magica_frame, (self.tamanho, self.tamanho))
        #             self.magica_frames.append(magica_frame)
        #         elif row == 0 and col == 3:
        #             frame_x = col * self.sprite_width
        #             frame_y = row * self.sprite_height
        #             magica_frame = self.spritesheet_magica.subsurface((frame_x, frame_y, self.sprite_width, self.sprite_height))
        #             magica_frame = pygame.transform.scale(magica_frame, (self.tamanho, self.tamanho))
        #             self.magica_frames.append(magica_frame)
                    
        # self.magica_img = self.magica_frames[0]
        # self.rect_magica = self.magica_img.get_rect()  
        
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

        # self.rect_magica.topleft = (self.x, self.y)
    
    def draw(self):
        pygame.draw.circle(self.game.screen, 'white', (self.x, self.y), (self.radius))
        # self.game.screen.blit(self.magica_frames[self.game.current_frame // self.game.frame_rate], (self.rect_magica.x, self.rect_magica.y))
        