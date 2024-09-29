import pygame
# from settings import *




_ = False
map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]

class Map:
    def __init__(self, game):
        self.game = game
        self.map = map
        self.world_map = {}
        self.get_map()
        self.pontos_string = "Pontuação: "
        self.vida_string = "Vidas: "
        # Carrega a fonte para exibir a pontuação
        self.font = pygame.font.Font(None, 36)
    
    def get_map(self):
        for j, linha in enumerate(self.map):
            for i, valor in enumerate(linha):
                if valor:
                    self.world_map[(i, j)] = valor

    def draw(self,jogador):
        for pos in self.world_map:
        # Verifica se a posição é da última linha do mapa
            if pos[1] == len(self.map) - 1:
                color = 'purple'  # Cor para a última linha
                pygame.draw.rect(self.game.screen, color, (pos[0] * 51.2, pos[1] * 51.25, 51.25, 51.25), 0)
                

            else:
                color = 'green'  # Cor para as outras linhas
                pygame.draw.rect(self.game.screen, color, (pos[0] * 51.2, pos[1] * 51.25, 51.25, 51.25), 2)
                

        # Renderiza a pontuação e vida e a exibe na tela
        hud_jogador = self.font.render((self.pontos_string + str(self.game.pontos) + "     " + self.vida_string + str(jogador.vida)), True, ('white'))
        # vida_tela = self.font.render((self.vida_string + str(jogador.vida)), True, ('white'))

        screen_width = self.game.screen.get_width()
        cent_hud = (screen_width - hud_jogador.get_width()) / 2

        self.game.screen.blit(hud_jogador,( (cent_hud, 680)))        
