import pygame
from pygame.sprite import Sprite 

class Bala(Sprite):
    def __init__(self, a_game):
        super().__init__() 
        self.screen = a_game.screen
        self.color = a_game.colorBala
        self.rect = pygame.Rect(0, 0, a_game.anchoBala, a_game.altoBala) #inicializa el rectangulo de la bala
        self.rect.midtop = a_game.nave.rect.midtop #desde donde queremos que salga la bala
        self.juego = a_game
        self.y = float(self.rect.y) #mas tipo de velocidad de bala
        self.enemigoPuntaje = 10
        self.sonido = pygame.mixer.Sound("C:\\Users\\Sarop\\OneDrive\\Escritorio\\pygame\\sonido\\sonido_disparo.mp3")
        self.sonido.play()
        
    def update(self): #posicion de la bala
        self.y -= self.juego.velocidad
        self.rect.y = self.y
        self.bala = self.juego.bala
        self.enemigo = self.juego.enemigo

        self.choques = pygame.sprite.groupcollide(self.bala, self.enemigo, True, True)

        if self.choques: #suma de puntaje cuando una bala choca con enemigo
            for enemigo in self.choques.values():
                self.juego.score += self.enemigoPuntaje * len(enemigo)
                self.juego.tablaP.prep_score()
                self.juego.tablaP.checa_HighScore()

    def dibujar_bala(self):
        pygame.draw.rect(self.screen, self.color, self.rect)