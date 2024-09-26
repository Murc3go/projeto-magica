import pygame
from settings import *


class Menu:
    def __init__(self,screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 55)
        self.menu_ativo = True
    
    def mostrar_menu(self):
        while self.menu_ativo:
            self.screen.fill('black')
            title_text = self.font.render("Projeto Mágica", True, (255, 255, 255))
            start_text = self.font.render("Pressione 'S' para Iniciar", True, (255, 255, 255))
            exit_text = self.font.render("Pressione 'E' para Sair", True, (255, 255, 255))

            self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, 100))
            self.screen.blit(start_text, (self.screen.get_width() // 2 - start_text.get_width() // 2, 300))
            self.screen.blit(exit_text, (self.screen.get_width() // 2 - exit_text.get_width() // 2, 400))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:  # Começar o jogo
                        self.menu_ativo = False
                    if event.key == pygame.K_e:  # Sair do jogo
                        pygame.quit()
                        exit()