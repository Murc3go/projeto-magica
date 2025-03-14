import pygame
import random
import math


class Item(pygame.sprite.Sprite):
    def __init__(self, game, x, y, item_caminho):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.x = x
        self.y = y
        self.spritesheet = pygame.image.load(item_caminho).convert_alpha()
        self.sprite_sombra = pygame.transform.scale(pygame.image.load("Sprites/Particulas/sombra.png"), (15, 10))
        self.sombra_rect = self.sprite_sombra.get_rect(topleft=(self.x + 2, self.y + 15))
        self.animation_speed = 0.5
        self.timer = 0
        self.frames = []
        self.frame_index = 0
        self.largura = 20
        self.altura = 20
        frame_wd = self.spritesheet.get_width() // 4
        frame_ht = self.spritesheet.get_height()

        for i in range(4):
            frame = self.spritesheet.subsurface((i * frame_wd, 0, frame_wd, frame_ht)).convert_alpha()
            frame = pygame.transform.scale(frame, (self.largura,self.altura))
            self.frames.append(frame)

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    
    def acerto_jogador(self, jogador):
        return self.rect.colliderect(jogador.rect)

    def update(self, dt):
        self.timer += dt  # Acumula o tempo decorrido

        if self.timer >= self.animation_speed:  
            self.timer = 0  # Reinicia o timer
            self.frame_index = (self.frame_index + 1) % len(self.frames)  # Avança o frame
            self.image = self.frames[self.frame_index]  # Atualiza a imagem

    def draw(self):
        self.game.screen.blit(self.sprite_sombra, self.sombra_rect)
        self.game.screen.blit(self.image, self.rect.topleft)

class ItemMoeda(Item):

    def efeito(self):
        self.game.moedas += 1
    