import pygame


class Botao:
    def __init__(self, y,texto, screen):
        self.screen = screen
        self.y = y
        self.fonte = pygame.font.Font("Font/NormalFont.ttf", 20)
        self.texto = self.fonte.render(texto, True, ('white'))
        self.texto_wd = self.texto.get_width()
        self.clicado = False
        self.sprite_normal = pygame.transform.scale(pygame.image.load("Sprites/PainelMenu/Botões/button_normal.png"), (200, 80))
        self.sprite_hover = pygame.transform.scale(pygame.image.load("Sprites/PainelMenu/Botões/button_hover.png"), (200, 80))
        self.sprite_pressed = pygame.transform.scale(pygame.image.load("Sprites/PainelMenu/Botões/button_pressed.png"), (200, 80))
        self.sprite = self.sprite_normal
        self.sprite_rect = self.sprite.get_rect(center=(self.screen.get_width() // 2, self.y))
        self.texto_y = self.sprite_rect.centery - self.texto.get_height() // 2 - 5
        self.texto_y_atual = self.texto_y

    def draw(self):
        self.screen.blit(self.sprite, self.sprite_rect)
        text_x = self.sprite_rect.centerx - self.texto.get_width() // 2
        self.screen.blit(self.texto, (text_x, self.texto_y_atual))
  
    
    def checar_interacao(self, evento):
        mouse_pos = pygame.mouse.get_pos()

        if self.sprite_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.sprite = self.sprite_pressed
                self.texto_y_atual = self.sprite_rect.centery - self.texto.get_height() // 2 + 2
                self.clicado = True
            else:
                self.sprite = self.sprite_hover
                self.texto_y_atual = self.sprite_rect.centery - self.texto.get_height() // 2 - 5
        else:
            self.sprite = self.sprite_normal
            self.texto_y_atual = self.sprite_rect.centery - self.texto.get_height() // 2 - 5

        if evento.type == pygame.MOUSEBUTTONUP and self.clicado:
            self.clicado = False
            return True
        return False
class Menu:
    def __init__(self,screen):
        self.screen = screen
        self.fonte = pygame.font.Font("Font/NormalFont.ttf", 40)
        
        self.menu_ativo = True
        self.sprite = pygame.transform.scale(pygame.image.load('Sprites/PainelMenu/menu-inicial.png'), (self.screen.get_width(), self.screen.get_height()))
        self.botao_start = Botao(300,"INICIAR", self.screen)
        self.botao_exit = Botao(400, "SAIR", self.screen)
    def mostrar_menu(self):
        while self.menu_ativo:
            self.screen.blit(self.sprite, (0, 0))
            title_text = self.fonte.render("PROJETO     MAGICA", True, ('white'))
            self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, 150)) 
            self.botao_start.draw()
            self.botao_exit.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                if self.botao_start.checar_interacao(event):
                    self.menu_ativo = False
   
                if self.botao_exit.checar_interacao(event):
                        pygame.quit()
                        exit()

class GameOver:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.font = pygame.font.SysFont(None, 55)
        
    def mostrar_game_over(self):
        while self.game.game_over:
            self.screen.fill('black')
            game_over_text = self.font.render("Fim de Jogo", True, (255, 255, 255))
            restart_text = self.font.render("Pressione 'S' para Reiniciar", True, (255, 255, 255))
            exit_text = self.font.render("Pressione 'E' para Sair", True, (255, 255, 255))

            self.screen.blit(game_over_text, (self.screen.get_width() // 2 - game_over_text.get_width() // 2, 100))
            self.screen.blit(restart_text, (self.screen.get_width() // 2 - restart_text.get_width() // 2, 300))
            self.screen.blit(exit_text, (self.screen.get_width() // 2 - exit_text.get_width() // 2, 400))
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.game.game_over = False
                        self.game.new_game()
                    if event.key == pygame.K_e:
                        pygame.quit()
                        exit()