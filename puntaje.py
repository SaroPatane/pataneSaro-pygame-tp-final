import pygame.font
from pygame.sprite import Group
from vida import Vidas


class TablaPuntajes():
    def __init__(self, a_game):
        self.screen = a_game.screen
        self.screen_rect = self.screen.get_rect()
        self.juego = a_game
        self.estadisticas = a_game.estadisticas

        self.colorTexto = (255, 219, 219)
        self.font = pygame.font.SysFont(None, 50)
        self.prep_score()
        self.prep_HighScore()
        self.prep_vidas()

    def prep_score(self): #puntaje por juego
        self.scoreStr = str(self.juego.score)
        self.scoreImagen = self.font.render(self.scoreStr, True, self.colorTexto, None,)
    
        self.score_rect = self.scoreImagen.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_HighScore(self): #puntaje mas alto
        self.HighScoreStr = str(self.juego.HighScore)
        self.HighScoreImagen = self.font.render(self.HighScoreStr, True, self.colorTexto, None)

        self.HighScore_rect = self.HighScoreImagen.get_rect()
        self.HighScore_rect.centerx = self.screen_rect.centerx
        self.HighScore_rect.top = self.screen_rect.top
        
    def checa_HighScore(self): #deja el puntaje mas alto
        if self.juego.score > self.juego.HighScore:
            self.juego.HighScore = self.juego.score
            self.prep_HighScore()

    def muestraScore(self): #muestra puntaje en pantalla
        self.screen.blit(self.scoreImagen, self.score_rect)
        self.screen.blit(self.HighScoreImagen, self.HighScore_rect)
        self.vidas.draw(self.screen)
    
    def prep_vidas(self): #muestra las vidas de la nave
        self.vidas = Group()
        for numero_vidas in range(self.juego.naves_restantes):
            vida = Vidas(self.juego)
            vida.rect.x = 10 * numero_vidas * 7
            vida.rect.y = 10
            self.vidas.add(vida)
    
