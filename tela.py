import pygame

        

class Map(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.tile_size_wd = 32 # Tamanho do quadrado
        self.tile_size_ht = 32 # Tamanho do quadrado
        self.cerca_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/Cenario/cerca.png'), (self.tile_size_wd, self.tile_size_ht))
        self.grass_chao_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/Outono/outono10.png'), (self.tile_size_wd, self.tile_size_ht))
        self.grass_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/Cenario/grass4.png'), (self.tile_size_wd, self.tile_size_ht))
        self.bar_esq_sup_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/Outono/outono01.png'), (self.tile_size_wd, self.tile_size_ht))
        self.bar_esq_inf_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/Outono/outono02.png'), (self.tile_size_wd, self.tile_size_ht))
        self.bar_dir_sup_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/Outono/outono03.png'), (self.tile_size_wd, self.tile_size_ht))
        self.bar_dir_inf_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/Outono/outono04.png'), (self.tile_size_wd, self.tile_size_ht))
        self.bar_sup_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/Outono/outono05.png'), (self.tile_size_wd, self.tile_size_ht))
        self.bar_inf_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/Outono/outono06.png'), (self.tile_size_wd, self.tile_size_ht))
        self.bar_esq_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/Outono/outono07.png'), (self.tile_size_wd, self.tile_size_ht))
        self.bar_dir_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/Outono/outono08.png'), (self.tile_size_wd, self.tile_size_ht))
        self.chao_sprite = pygame.transform.scale(pygame.image.load('Sprites/Tileset/Outono/outono09.png'), (self.tile_size_wd, self.tile_size_ht))
        self.hud_sprite = pygame.transform.scale(pygame.image.load('Sprites/Painel/painel3.png'), (self.tile_size_wd, self.tile_size_ht))
        self.hud_esq_sprite = pygame.transform.scale(pygame.image.load('Sprites/Painel/painel1.png'), (self.tile_size_wd, self.tile_size_ht))
        self.hud_dir_sprite = pygame.transform.scale(pygame.image.load('Sprites/Painel/painel2.png'), (self.tile_size_wd, self.tile_size_ht))
        self.game = game
        self.map_layout = [
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5],
        [5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5],
        [5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ]
        self.pontos_string = "Pontuação: "
        self.vida_string = "Vidas: "
        self.font = pygame.font.Font("Font/NormalFont.ttf", 20)
        self.map_surface = pygame.Surface((1024, 768))
        for y, row in enumerate(self.map_layout):
            for x, tile in enumerate(row):
                if tile == 1:
                    self.map_surface.blit(self.grass_chao_sprite, (x * self.tile_size_wd, y * self.tile_size_ht))
                    self.map_surface.blit(self.grass_sprite, (x * self.tile_size_wd, y * self.tile_size_ht))

                elif tile == 2:
                    if (x == 1 and y == 1):
                        self.map_surface.blit(self.bar_esq_sup_sprite, (x * self.tile_size_wd, y * self.tile_size_ht))
                        
                    elif(x == len(row) - 2 and y == 1):
                        self.map_surface.blit(self.bar_dir_sup_sprite, (x * self.tile_size_wd, y * self.tile_size_ht))
                        
                    elif(x == 1 and y == len(self.map_layout) - 3): 
                        self.map_surface.blit(self.bar_esq_inf_sprite, (x * self.tile_size_wd, y * self.tile_size_ht))
                        
                    elif(x == len(row) - 2 and y == len(self.map_layout) - 3):
                        self.map_surface.blit(self.bar_dir_inf_sprite, (x * self.tile_size_wd, y * self.tile_size_ht)) 
                         
                    elif(x == 1):
                        self.map_surface.blit(self.bar_esq_sprite, (x * self.tile_size_wd, y * self.tile_size_ht))
                        
                    elif(y == 1):
                        self.map_surface.blit(self.bar_sup_sprite, (x * self.tile_size_wd, y * self.tile_size_ht))
                        
                    elif(y == len(self.map_layout) - 3):   
                        self.map_surface.blit(self.bar_inf_sprite, (x * self.tile_size_wd, y * self.tile_size_ht))
                        
                    elif(x == len(row) - 2):
                        self.map_surface.blit(self.bar_dir_sprite, (x * self.tile_size_wd, y * self.tile_size_ht))
                        
                elif tile == 3:
                    if(y == len(self.map_layout) - 1):
                        self.map_surface.blit(self.hud_sprite, (x * self.tile_size_wd, self.game.screen.get_height() - self.tile_size_ht))   
                    if(x == 0 and y == len(self.map_layout) - 1):
                        self.map_surface.blit(self.hud_esq_sprite, (0, self.game.screen.get_height() - self.tile_size_ht))
                    if(x == len(row) - 1 and y == len(self.map_layout) - 1):
                        self.map_surface.blit(self.hud_dir_sprite, (x * self.tile_size_wd, self.game.screen.get_height() - self.tile_size_ht))
                elif tile == 4:
                    self.map_surface.blit(self.grass_chao_sprite, (x * self.tile_size_wd, y * self.tile_size_ht))
                    self.map_surface.blit(self.cerca_sprite, (x * self.tile_size_wd, y * self.tile_size_ht))
                elif tile == 5:
                    self.map_surface.blit(self.grass_chao_sprite, (x * self.tile_size_wd, y * self.tile_size_ht))
                else:
                    self.map_surface.blit(self.chao_sprite, (x * self.tile_size_wd, y * self.tile_size_ht))

    def draw(self, jogador):
        self.game.screen.blit(self.map_surface, (0, 0))

        # Renderiza a pontuação e vida
        hud_jogador = self.font.render((self.pontos_string + str(self.game.pontos) + "     " + self.vida_string + str(jogador.vida)), True, ('white'))
        screen_width = self.game.screen.get_width()
        cent_hud = (screen_width - hud_jogador.get_width()) / 2
        self.game.screen.blit(hud_jogador, (cent_hud, 735))
