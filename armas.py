import pygame

class Balas:
    def __init__(self, game, x , y, direction_x, direction_y):
        self.game = game
        self.x = x
        self.y = y
        self.speed = 6
        self.radius = 5
        self.direction_x = direction_x
        self.direction_y = direction_y
        
    def update(self):
        self.y += self.direction_y * self.speed
        self.x += self.direction_x * self.speed
    
    def draw(self):
        pygame.draw.circle(self.game.screen, 'yellow', (self.x, self.y), (self.radius))