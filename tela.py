import pygame

        

class Map(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.tile_size = 55 # Tamanho do quadrado
        self.bar_esq_sup_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/l0_textura_terra01.png'), (self.tile_size, self.tile_size))
        self.bar_esq_inf_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/l0_textura_terra11.png'), (self.tile_size, self.tile_size))
        self.bar_dir_sup_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/l0_textura_terra03.png'), (self.tile_size, self.tile_size))
        self.bar_dir_inf_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/l0_textura_terra13.png'), (self.tile_size, self.tile_size))
        self.bar_sup_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/l0_textura_terra02.png'), (self.tile_size, self.tile_size))
        self.bar_inf_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/l0_textura_terra12.png'), (self.tile_size, self.tile_size))
        self.bar_esq_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/l0_textura_terra06.png'), (self.tile_size, self.tile_size))
        self.bar_dir_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/l0_textura_terra08.png'), (self.tile_size, self.tile_size))
        self.chao_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/l0_textura_terra07.png'), (self.tile_size, self.tile_size))
        self.hud_sprite = pygame.transform.scale(pygame.image.load('Sprites/Painel/painel3.png'), (self.tile_size, self.tile_size))
        self.hud_esq_sprite = pygame.transform.scale(pygame.image.load('Sprites/Painel/painel1.png'), (self.tile_size, self.tile_size))
        self.hud_dir_sprite = pygame.transform.scale(pygame.image.load('Sprites/Painel/painel2.png'), (self.tile_size, self.tile_size))
        self.game = game
        self.map_layout = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],]
        self.pontos_string = "Pontuação: "
        self.vida_string = "Vidas: "
        self.font = pygame.font.Font("Font/NormalFont.ttf", 24)
        self.map_surface = pygame.Surface((1366, 768))
        for y, row in enumerate(self.map_layout):
            for x, tile in enumerate(row):
                if tile == 1:
                    if (x == 0 and y == 0):
                        self.map_surface.blit(self.bar_esq_sup_sprite, (x * self.tile_size, y * self.tile_size))
                    elif(x == len(row) - 1 and y == 0):
                        self.map_surface.blit(self.bar_dir_sup_sprite, (x * self.tile_size, y * self.tile_size))
                    elif(x == 0 and y == len(self.map_layout) - 2): 
                        self.map_surface.blit(self.bar_esq_inf_sprite, (x * self.tile_size, y * self.tile_size))
                    elif(x == len(row) - 1 and y == len(self.map_layout) - 2):
                        self.map_surface.blit(self.bar_dir_inf_sprite, (x * self.tile_size, y * self.tile_size))  
                    elif(x == 0):
                        self.map_surface.blit(self.bar_esq_sprite, (x * self.tile_size, y * self.tile_size))
                    elif(y == 0):
                        self.map_surface.blit(self.bar_sup_sprite, (x * self.tile_size, y * self.tile_size))
                    elif(y == len(self.map_layout) - 2):   
                        self.map_surface.blit(self.bar_inf_sprite, (x * self.tile_size, y * self.tile_size))
                    elif(x == len(row) - 1):
                        self.map_surface.blit(self.bar_dir_sprite, (x * self.tile_size, y * self.tile_size))
                elif tile == 3:
                    if(y == len(self.map_layout) - 1):
                        self.map_surface.blit(self.hud_sprite, (x * self.tile_size, self.game.screen.get_height() - self.tile_size))   
                    if(x == 0 and y == len(self.map_layout) - 1):
                        self.map_surface.blit(self.hud_esq_sprite, (0, self.game.screen.get_height() - self.tile_size))
                    if(x == len(row) - 1 and y == len(self.map_layout) - 1):
                        self.map_surface.blit(self.hud_dir_sprite, (x * self.tile_size, self.game.screen.get_height() - self.tile_size))
                else:
                    self.map_surface.blit(self.chao_sprite, (x * self.tile_size, y * self.tile_size))

    def draw(self, jogador):
        self.game.screen.blit(self.map_surface, (0, 0))

        # Renderiza a pontuação e vida
        hud_jogador = self.font.render((self.pontos_string + str(self.game.pontos) + "     " + self.vida_string + str(jogador.vida)), True, ('white'))
        screen_width = self.game.screen.get_width()
        cent_hud = (screen_width - hud_jogador.get_width()) / 2
        self.game.screen.blit(hud_jogador, (cent_hud, 723))
