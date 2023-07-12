import pygame 
import sys
from nave import Nave
from bala import Bala
from enemigo import Enemigo
from estadisticas import Estadisticas
from time import sleep
from boton import Boton
from puntaje import TablaPuntajes



class Juego:
    def __init__(self):
        #variables
        pygame.init()
        self.score = 0
        self.HighScore = 0
        self.ancho = 1200
        self.alto = 600
        self.screen = pygame.display.set_mode((self.ancho, self.alto)) 
        pygame.display.set_caption("Naves de la Galaxia")
        self.fondo = pygame.image.load("C:\\Users\\Sarop\\OneDrive\\Escritorio\\pygame\\imagenes\\fondo estrellado.png").convert()
        self.velocidad = 1
        self.anchoBala = 3
        self.altoBala = 15
        self.colorBala = (255, 0, 0)
        self.naves_restantes = 3
        self.velocidad_nave = 1
        self.estadisticas = Estadisticas(self)
        self.tablaP = TablaPuntajes(self)
        self.nave = Nave(self)
        self.bala = pygame.sprite.Group()
        self.enemigo = pygame.sprite.Group()
        self.velocidad_enemigo = 1.0
        self.flota_velocidad = 10
        self.flota_direccion = 1
        self.juego_activado = False
        self.play_boton = Boton(self, "Play")
        self.velocidad_aumentada = 1.2
        self.valoresDefault()
        
        #musica
        pygame.mixer.music.load("C:\\Users\\Sarop\\OneDrive\\Escritorio\\pygame\\musica\\lady-of-the-80x27s-128379.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        self._crear_flota() #crea la flota, linea 96
        
    def corre_juego(self):
        while True:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha = True
                    if event.key == pygame.K_LEFT:
                        self.nave.mover_izquierda = True
                    if event.key == pygame.K_SPACE:
                        self._disparo_bala()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.nave.mover_derecha = False
                    if event.key == pygame.K_LEFT:
                        self.nave.mover_izquierda = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.checaBoton(mouse_pos)
            
            if self.juego_activado:
                self.nave.mover()                    
                self.screen.blit(self.fondo, [0, 0])
                self.nave.corre()
                self.bala.update()
                self.update_enemigo()

                for bala in self.bala.copy():
                    if bala.rect.bottom <= 0:
                        self.bala.remove(bala) #borra balas cuando sale del plano
                        

                for bala in self.bala.sprites():
                    bala.dibujar_bala()
                self.enemigo.draw(self.screen)
                self.tablaP.muestraScore()
            
            if not self.juego_activado:
                self.play_boton.dibuja_boton()
            
            pygame.display.flip() 

    def _disparo_bala(self):  
        nueva_bala = Bala(self)
        self.bala.add(nueva_bala)    

    def _crear_flota(self): #flota enemiga
        enemigo = Enemigo(self)
        enemigo_width, enemigo_height = enemigo.rect.size
        espacio_disponible_x = self.ancho - (2 * enemigo_width)
        numero_enemigos = espacio_disponible_x // (2 * enemigo_width)
        nave_height = self.nave.rect.height
        espacio_disponible_y = self.alto - (3 * enemigo_height) - nave_height
        numero_enemigo =  espacio_disponible_y // (2 * enemigo_height)

        for enemigo in range(numero_enemigo):
            for numeroEnemigo in range(numero_enemigos):
                self._crear_enemigo(numeroEnemigo, enemigo)

    def _crear_enemigo(self, numeroEnemigo, fila):
        enemigo = Enemigo(self)
        enemigo_width, enemigo_height = enemigo.rect.size
        enemigo.x = enemigo_width + 2 * enemigo_width * numeroEnemigo
        enemigo.rect.x = enemigo.x
        enemigo.rect.y = enemigo.rect.height + 2 * enemigo.rect.height * fila
        self.enemigo.add(enemigo)
    
    def update_enemigo(self):
        self.checa_bordesFlota()
        self.enemigo.update()
        if not self.enemigo:
            self.aumentaVelocidad()
            self._crear_flota()
        if pygame.sprite.spritecollideany(self.nave, self.enemigo):
             self.nave_colisionada()

    def nave_colisionada(self):
        if self.naves_restantes > 0:

            self.naves_restantes -= 1
            self.tablaP.prep_vidas()

            self.enemigo.empty()
            
            self._crear_flota()
            self.nave.centrar_nave()

            sleep(0.5)
        else:
            self.juego_activado = False
    
    def checaBoton(self, mouse_pos):
        self.boton_play = self.play_boton.rect.collidepoint(mouse_pos)
        if self.boton_play and not self.juego_activado:
            self.valoresDefault()
            self.estadisticas.reinicia()
            self.juego_activado = True
            self.score = 0
            self.tablaP.prep_score()
            self.naves_restantes = 3
            self.tablaP.prep_vidas()

            self.enemigo.empty()

            self._crear_flota()
            self.nave.centrar_nave()
    
    def checa_bordesFlota(self):
        for enemigo in self.enemigo.sprites():
            if enemigo.checa_bordes():
                self.cambia_direccion()
                break

    def cambia_direccion(self):
        for enemigo in self.enemigo.sprites():
            enemigo.rect.y += self.flota_velocidad
        self.flota_direccion *= -1
    
    def valoresDefault(self):
        self.velocidad_nave = 1
        self.velocidad = 1
        self.velocidad_enemigo = 1.0
        self.flota_direccion = 1

    def aumentaVelocidad(self):
        self.velocidad_nave *= self.velocidad_aumentada
        self.velocidad *= self.velocidad_aumentada
        self.velocidad_enemigo *= self.velocidad_aumentada
            

if __name__ == "__main__":
    a = Juego()
    a.corre_juego()
