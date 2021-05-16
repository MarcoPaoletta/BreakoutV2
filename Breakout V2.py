# Import

import pygame,sys,time

# Pantalla

ANCHO = 640
ALTO = 480

# Colores

blanco = (213, 216, 220 )
azul = (0,0,255)
negro = (0,0,0)
rosa = (219, 112, 147)
azul_oscuro = (21, 50, 96)
cian = (26, 70, 118)
celeste = (31, 120, 141)
amarillo = (244, 208, 63 )
negro = (23, 32, 42)
gris = (28, 40, 51)
gris_claro = (33, 47, 61)
# Inicializar pygame

pygame.init()

# Bolita

class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bolita1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        self.speed = [5,5]

    def update(self):
        if self.rect.top <= 0:
            self.speed[1] =- self.speed[1]
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        self.rect.move_ip(self.speed)

# Jugador

class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('paleta1.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = (480,ALTO-20)
        self.speed = [0,0]

    def update(self,evento):
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-13,0]
        elif evento.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [13,0]
        else:
            self.speed = [0,0]
        self.rect.move_ip(self.speed)

# Ladrillo

class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ladrillo1.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion

# Muro

class Muro(pygame.sprite.Group):
    def __init__(self, cantidadLadrillos):
        pygame.sprite.Group.__init__(self)
        pos_x = 0
        pos_y = 0
        for i in range(cantidadLadrillos):
            ladrillo = Ladrillo((pos_x,pos_y))
            self.add(ladrillo)
            pos_x += ladrillo.rect.width

# Ladrillo 2

class Ladrillo2(pygame.sprite.Sprite):
    def __init__(self,posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ladrillo2.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion

# Muro 2

class Muro2(pygame.sprite.Group):
    def __init__(self, cantidadLadrillos2):
        pygame.sprite.Group.__init__(self)
        pos_x = 0
        pos_y = 20
        for i in range(cantidadLadrillos2):
            ladrillo2 = Ladrillo2((pos_x,pos_y))
            self.add(ladrillo2)
            pos_x += ladrillo2.rect.width

# Ladrillo 3

class Ladrillo3(pygame.sprite.Sprite):
    def __init__(self,posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ladrillo3.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion

# Muro 3

class Muro3(pygame.sprite.Group):
    def __init__(self, cantidadLadrillos3):
        pygame.sprite.Group.__init__(self)
        pos_x = 0
        pos_y = 40
        for i in range(cantidadLadrillos3):
            ladrillo3 = Ladrillo3((pos_x,pos_y))
            self.add(ladrillo3)
            pos_x += ladrillo3.rect.width

# Ladrillo 4

class Ladrillo4(pygame.sprite.Sprite):
    def __init__(self,posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ladrillo4.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion

# Muro 4

class Muro4(pygame.sprite.Group):
    def __init__(self, cantidadLadrillos4):
        pygame.sprite.Group.__init__(self)
        pos_x = 0
        pos_y = 60
        for i in range(cantidadLadrillos4):
            ladrillo4 = Ladrillo4((pos_x,pos_y))
            self.add(ladrillo4)
            pos_x += ladrillo4.rect.width

# Ladrillo 5

class Ladrillo5(pygame.sprite.Sprite):
    def __init__(self,posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ladrillo5.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion

# Muro 5

class Muro5(pygame.sprite.Group):
    def __init__(self, cantidadLadrillos5):
        pygame.sprite.Group.__init__(self)
        pos_x = 0
        pos_y = 80
        for i in range(cantidadLadrillos5):
            ladrillo5 = Ladrillo5((pos_x,pos_y))
            self.add(ladrillo5)
            pos_x += ladrillo5.rect.width

# Jugador 2

class Paleta2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('paleta2.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = (160,ALTO-20)
        self.speed = [0,0]

    def update(self,evento):
        if evento.key == pygame.K_a and self.rect.left > 0:
            self.speed = [-13,0]
        elif evento.key == pygame.K_d and self.rect.right < ANCHO:
            self.speed = [13,0]
        else:
            self.speed = [0,0]
        self.rect.move_ip(self.speed)

# Bolita 2

class Bolita2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bolita2.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        self.speed = [5,5]

    def update(self):
        if self.rect.top <= 0:
            self.speed[1] =- self.speed[1]
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        self.rect.move_ip(self.speed)

# Juego terminado

def juego_terminado():
    fuente = pygame.font.SysFont("Arial",50)
    texto = fuente.render("Juego terminado, perdiste", True,blanco)
    texto_rect = texto.get_rect()
    texto_rect.center = [ANCHO / 2, ALTO / 2]
    pantalla.blit(texto,texto_rect)
    pygame.display.flip()
    time.sleep(3)
    sys.exit()

# Mostrar puntuacion

def mostrar_puntuacion():
    fuente = pygame.font.SysFont("Consolas",15)
    cadena = "Puntuacion: " + str(puntuacion)
    texto = fuente.render(cadena, True,amarillo)
    texto_rect = texto.get_rect()
    texto_rect.bottomright = [ANCHO, ALTO]
    pantalla.blit(texto,texto_rect)

# Mostrar vidas

def mostrar_vidas():
    fuente = pygame.font.SysFont("Consolas",15)
    cadena = "Vidas: " + str(vidas)
    texto = fuente.render(cadena, True,amarillo)
    texto_rect = texto.get_rect()
    texto_rect.bottomleft = [0,ALTO]
    pantalla.blit(texto,texto_rect)

# Final

def Final():
    fuente = pygame.font.SysFont("Arial",50)
    texto = fuente.render("Juego completado,ganaste", True,blanco)
    texto_rect = texto.get_rect()
    texto_rect.center = [ANCHO / 2, ALTO / 2]
    pantalla.blit(texto,texto_rect)
    pygame.display.flip()
    time.sleep(4.1)
    sys.exit()
# Tamaño pantalla e inicializando

pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Configurar título de pantalla.

pygame.display.set_caption('Juego de ladrillos')

# FPS

reloj = pygame.time.Clock()

# Repeticion de eventos

pygame.key.set_repeat(30)

# Elementos
    # Marcadores
puntuacion = 0
vidas = 3
    # Bolitas
bolita = Bolita()
bolita2 = Bolita2()
    # Jugadores
jugador = Paleta()
jugador2 = Paleta2()
    # Muros
muro = Muro(16)
muro2 = Muro2(16)
muro3 = Muro3(16)
muro4 = Muro4(16)
muro5 = Muro5(16)
    # Esperando saques
esperando_saque = True
esperando_saque2 = True

# Sonidos
    # Ladrillo roto

ladrillo_roto = pygame.mixer.Sound("ladrillo_roto.mp3")
derrota = pygame.mixer.Sound("derrota.mp3")
victoria = pygame.mixer.Sound("victoria.mp3")

    # Musica

pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(1000000)
pygame.mixer.music.get_volume
pygame.mixer.music.set_volume(0.30)

# Main loop

while True:
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        # Eventos teclado
            # Movimiento j1 y j2
        if evento.type == pygame.KEYDOWN:
            jugador.update(evento)
            if esperando_saque == True and evento.key == pygame.K_UP:
                esperando_saque = False
                if bolita.rect.centerx < ANCHO / 2:
                    bolita.speed = [5,-5]
                else:
                    bolita.speed = [-5,-5]
        if evento.type == pygame.KEYDOWN:
            jugador2.update(evento)

            # Esperando saque j2
            if esperando_saque2 == True and evento.key == pygame.K_w:
                esperando_saque2 = False
                if bolita2.rect.centerx < ANCHO / 2:
                    bolita2.speed = [5,-5]
                else:
                    bolita2.speed = [-5,-5]

    # Revisar si la bolita sale de la pantalla
        # Bolita 1
    if bolita.rect.top > ALTO:
        vidas -= 1
        esperando_saque = True
        # Bolita 2
    if bolita2.rect.top > ALTO:
        vidas -= 1
        esperando_saque2 = True

    # Esperando saque
        # Esperando saque 1
    if esperando_saque == False:
        bolita.update()
    else:
        bolita.rect.midbottom = jugador.rect.midtop
        # Esperando saque 2
    if esperando_saque2 == False:
        bolita2.update()
    else:
        bolita2.rect.midbottom = jugador2.rect.midtop

    # Nivel de la musica segun vidas

    if vidas <= 2:
        pygame.mixer.music.set_volume(0.60)
    if vidas <= 1:
        pygame.mixer.music.set_volume(1)

    # Colision entre bolita y jugador
        # B1 y J1
    if pygame.sprite.collide_rect(bolita,jugador):
        bolita.speed[1] =-bolita.speed[1]
        # B2 y J2
    if pygame.sprite.collide_rect(bolita2,jugador2):
        bolita2.speed[1] =-bolita2.speed[1]
        # B1 y J2
    if pygame.sprite.collide_rect(bolita,jugador2):
        bolita.speed[1] =-bolita.speed[1]
        # B2 y J1
    if pygame.sprite.collide_rect(bolita2,jugador):
        bolita2.speed[1] =-bolita2.speed[1]

    # Colisiones entre bolita 1 y muro

        # Muro 1

    colision_jugador_muro = pygame.sprite.spritecollide(bolita,muro,False)
    if colision_jugador_muro:
        ladrillo = colision_jugador_muro[0]
        cx = bolita.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            bolita.speed[0] =- bolita.speed[0]
        else:
            bolita.speed[1] =- bolita.speed[1]
        muro.remove(ladrillo)
        puntuacion += 1
        ladrillo_roto.play()

        # Muro 2

    colision_jugador_muro2 = pygame.sprite.spritecollide(bolita,muro2,False)
    if colision_jugador_muro2:
        ladrillo2 = colision_jugador_muro2[0]
        cx = bolita.rect.centerx
        if cx < ladrillo2.rect.left or cx > ladrillo2.rect.right:
            bolita.speed[0] =- bolita.speed[0]
        else:
            bolita.speed[1] =- bolita.speed[1]
        muro2.remove(ladrillo2)
        puntuacion += 1
        ladrillo_roto.play()

        # Muro 3

    colision_jugador_muro3 = pygame.sprite.spritecollide(bolita,muro3,False)
    if colision_jugador_muro3:
        ladrillo3 = colision_jugador_muro3[0]
        cx = bolita.rect.centerx
        if cx < ladrillo3.rect.left or cx > ladrillo3.rect.right:
            bolita.speed[0] =- bolita.speed[0]
        else:
            bolita.speed[1] =- bolita.speed[1]
        muro3.remove(ladrillo3)
        puntuacion += 1
        ladrillo_roto.play()

        # Muro 4

    colision_jugador_muro4 = pygame.sprite.spritecollide(bolita,muro4,False)
    if colision_jugador_muro4:
        ladrillo4 = colision_jugador_muro4[0]
        cx = bolita.rect.centerx
        if cx < ladrillo4.rect.left or cx > ladrillo4.rect.right:
            bolita.speed[0] =- bolita.speed[0]
        else:
            bolita.speed[1] =- bolita.speed[1]
        muro4.remove(ladrillo4)
        puntuacion += 1
        ladrillo_roto.play()

        # Muro 5

    colision_jugador_muro5 = pygame.sprite.spritecollide(bolita,muro5,False)
    if colision_jugador_muro5:
        ladrillo5 = colision_jugador_muro5[0]
        cx = bolita.rect.centerx
        if cx < ladrillo5.rect.left or cx > ladrillo5.rect.right:
            bolita.speed[0] =- bolita.speed[0]
        else:
            bolita.speed[1] =- bolita.speed[1]
        muro5.remove(ladrillo5)
        puntuacion += 1
        ladrillo_roto.play()

    # Colisiones entre bolita 2 y muro
        # Muro 1
    colision_jugador2_muro = pygame.sprite.spritecollide(bolita2,muro,False)
    if colision_jugador2_muro:
        ladrillo = colision_jugador2_muro[0]
        cx = bolita2.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            bolita2.speed[0] =- bolita2.speed[0]
        else:
            bolita2.speed[1] =- bolita2.speed[1]
        muro.remove(ladrillo)
        puntuacion += 1
        ladrillo_roto.play()
        # Muro 2
    colision_jugador2_muro2 = pygame.sprite.spritecollide(bolita2,muro2,False)
    if colision_jugador2_muro2:
        ladrillo = colision_jugador2_muro2[0]
        cx = bolita2.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            bolita2.speed[0] =- bolita2.speed[0]
        else:
            bolita2.speed[1] =- bolita2.speed[1]
        muro2.remove(ladrillo)
        puntuacion += 1
        ladrillo_roto.play()
            # Muro 3
    colision_jugador2_muro3 = pygame.sprite.spritecollide(bolita2,muro3,False)
    if colision_jugador2_muro3:
        ladrillo = colision_jugador2_muro3[0]
        cx = bolita2.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            bolita2.speed[0] =- bolita2.speed[0]
        else:
            bolita2.speed[1] =- bolita2.speed[1]
        muro3.remove(ladrillo)
        puntuacion += 1
        ladrillo_roto.play()
            # Muro 4
    colision_jugador2_muro4 = pygame.sprite.spritecollide(bolita2,muro4,False)
    if colision_jugador2_muro4:
        ladrillo = colision_jugador2_muro4[0]
        cx = bolita2.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            bolita2.speed[0] =- bolita2.speed[0]
        else:
            bolita2.speed[1] =- bolita2.speed[1]
        muro4.remove(ladrillo)
        puntuacion += 1
        ladrillo_roto.play()
            # Muro 5
    colision_jugador2_muro5 = pygame.sprite.spritecollide(bolita2,muro5,False)
    if colision_jugador2_muro5:
        ladrillo = colision_jugador2_muro5[0]
        cx = bolita2.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            bolita2.speed[0] =- bolita2.speed[0]
        else:
            bolita2.speed[1] =- bolita2.speed[1]
        muro5.remove(ladrillo)
        puntuacion += 1
        ladrillo_roto.play()

    # Rellanar pantalla segun vidas

    if vidas <= 3:
        pantalla.fill(negro)
    if vidas <= 2:
        pantalla.fill(gris)
    if vidas <= 1:
        pantalla.fill(gris_claro)

    # Mostar elementos en pantalla
        # Marcadores
    mostrar_puntuacion()
    mostrar_vidas()
        # Bolitas
    pantalla.blit(bolita.image, bolita.rect)
    pantalla.blit(bolita2.image,bolita2.rect)
        # Jugadores
    pantalla.blit(jugador.image,jugador.rect)
    pantalla.blit(jugador2.image,jugador2.rect)
        # Muros
    muro.draw(pantalla)
    muro2.draw(pantalla)
    muro3.draw(pantalla)
    muro4.draw(pantalla)
    muro5.draw(pantalla)

    # Actualizar los elementos en pantalla

    pygame.display.flip()

    # Final

    if puntuacion == 80:
        pygame.mixer.music.pause()
        victoria.play()
        Final()


    # Manejo vidas

    if vidas <= 0:
        pygame.mixer.music.pause()
        derrota.play()
        juego_terminado()