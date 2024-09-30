import pygame

class Spritesheet:
    def __init__(self,spritesheet_path, x, y):
        self.spritesheet = pygame.image.load(spritesheet_path).convert_alpha()
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.sprite_image = self.abrir_imagem()
    
    def abrir_imagem(self):
        # Cria uma superfície vazia
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        # Desenha o sprite da parte correspondente do spritesheet na nova superfície
        image.blit(self.spritesheet, (0, 0), (self.x, self.y, self.width, self.height))

        return image