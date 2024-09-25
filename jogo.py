import pygame
import sys
from settings import *
from tela import *
from jogador import *
from inimigos import *

class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(window_size)
        self.clock = pygame.time.Clock()
        self.new_game()
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.pontos = 0
        self.spawn_inimigos()
    
    def spawn_inimigos(self):
        self.inimigos = [Inimigo(self) for _ in range(2)]
    
    def update(self):
        # Atualiza a posição do player
        self.player.update()
        
        # Atualiza a posição dos inimigos
        for inimigo in self.inimigos:
            inimigo.update(self.player)
        
        if len(self.inimigos) == 0:
            self.spawn_inimigos()
        
     
        # Atualiza a tela
        pygame.display.flip()
        self.clock.tick(fps)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')
        
        
    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()
        for inimigo in self.inimigos:
            inimigo.draw()
        
    def check_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
              # Detecta clique do mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Botão esquerdo do mouse
                if event.button == 1:  
                    self.player.shoot()  
        
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
if __name__ == '__main__':
    game = Game()
    game.run()


