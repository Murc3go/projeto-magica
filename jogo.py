import pygame
import sys
from settings import *
from tela import *
from jogador import *
from inimigos import *
from menu import *
from dificuldade import *

class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(window_size)
        self.clock = pygame.time.Clock()
        self.menu = Menu(self.screen)
        self.menu_game_over = GameOver(self.screen, self)
        self.game_over = False
        self.current_frame = 0
        self.frame_rate = 10
        self.new_game()

              

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.pontos = 0
        self.num_inimigos = 2
        self.inimigo_speed = 2
        self.inimigos = [Inimigo(self, self.inimigo_speed) for _ in range(self.num_inimigos)]
        self.dificuldade = Dificuldade(self, self.inimigos)

        
    
    def spawn_inimigos(self):
        self.inimigos = [Inimigo(self, self.inimigo_speed) for _ in range(self.num_inimigos)]
        self.dificuldade.subindo_dificuldade()   
    def update(self):
        if not self.game_over:

            # Atualiza a posição do player
            self.player.update(self.inimigos)
        
            # Atualiza a posição dos inimigos
            for inimigo in self.inimigos:
                inimigo.update(self.player)

                if self.player.vida == 0:
                    self.game_over = True
                    self.menu_game_over.mostrar_game_over()
        
            if len(self.inimigos) == 0:
                self.spawn_inimigos()       
     
            # Atualiza a tela
            pygame.display.flip()
            self.clock.tick(fps)
            pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')
        
        
    def draw(self):

        self.map.draw(self.player)

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
                if event.button == 1 and not self.game_over:  
                    self.player.shoot()  
        
        self.current_frame += 1
        for inimigo in self.inimigos:
            if self.current_frame >= len(inimigo.frames) * self.frame_rate:
                self.current_frame = 0
        
    def run(self):
        self.menu.mostrar_menu()
        while True:
            self.check_events()
            if not self.game_over:
                self.update() 
                self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()


