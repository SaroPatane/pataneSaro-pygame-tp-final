import pygame
from pygame.sprite import Sprite

class Enemigo(Sprite):
    def __init__(self, a_game):
        super().__init__()
        self.screen = a_game.screen

        self.image = pygame.image.load("C:\\Users\\Sarop\\OneDrive\\Escritorio\\pygame\\imagenes\\personaje\\enemigo.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.juego = a_game 

    def update(self):
        self.x += (self.juego.velocidad_enemigo * self.juego.flota_direccion)
        self.rect.x = self.x
    
    def checa_bordes(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True