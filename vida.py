import pygame
from pygame.sprite import Sprite

class Vidas(Sprite):
    def __init__(self, a_game):
        super().__init__()
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()
        self.image = pygame.image.load("C:\\Users\\Sarop\\OneDrive\\Escritorio\\pygame\\imagenes\\personaje\\nave.png")
        self.rect = self.image.get_rect()