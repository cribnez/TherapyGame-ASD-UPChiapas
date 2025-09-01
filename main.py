#* =================================================================================
#* Juego Terapéutico - Versión para GitHub
#*
#* Este script es una versión del juego que no requiere un dispositivo serial
#* y funciona sin archivos de sonido para facilitar su ejecución y prueba.
#* El control se realiza mediante las teclas de flecha del teclado.
#*
#* Creado por: Selina Linette Vázquez Durante y [Otro Estudiante si aplica]
#* Asesor: Dr. Christian Roberto Ibáñez Nangüelú
#* Afiliación: Universidad Politécnica de Chiapas
#* =================================================================================

import pygame
import random
import time
#// import serial # La librería serial no se usa en este modo
#// import json

#* ---------------------------------------------------------------------------------
#* MODO DE CONTROL
#* Este script está configurado para usar siempre el teclado.
#* La lógica para el puerto serial se ha mantenido comentada como referencia.
#* ---------------------------------------------------------------------------------
USAR_PUERTO_SERIAL = False

#* Inicialización de Pygame
pygame.init()

#* Configuración de la pantalla del juego
width, height = 1366, 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego Terapéutico con Control por Teclado")

#* Definición de colores
white = (255, 255, 255)
black = (0, 0, 0)

#* Parámetros iniciales del jugador
player_x, player_y = width // 2, height // 2
speed = 8

# Inicializar el reloj de Pygame para controlar los FPS
clock = pygame.time.Clock()

#* =================================================================================
#* SECCIÓN DE CARGA DE ASSETS (IMÁGENES Y SONIDOS)
#* =================================================================================

#? Esta función intentará cargar un archivo de imagen.
#? Si no lo encuentra, imprimirá una advertencia pero no detendrá el juego.
def cargar_asset(ruta_archivo, escala=None):
    """
    * Carga un asset de imagen de forma segura.
    * @param ruta_archivo: La ruta al archivo de imagen (ej. 'assets/player.png').
    * @param escala: Una tupla (ancho, alto) para reescalar la imagen.
    * @returns: El objeto de imagen de Pygame o None si no se encuentra.
    """
    try:
        asset = pygame.image.load(ruta_archivo)
        if escala:
            asset = pygame.transform.scale(asset, escala)
        return asset
    except pygame.error:
        #! Advertencia: No se pudo encontrar el archivo de imagen en la ruta especificada.
        print(f"! ADVERTENCIA: No se pudo encontrar el archivo '{ruta_archivo}'. El juego continuará sin él.")
        return None

#* Cargando las imágenes de los personajes y objetos
player_image = cargar_asset('assets/player.png', (90, 100))
pig_image = cargar_asset('assets/cerdo.png')
dog_image = cargar_asset('assets/perro.png')
vaca_image = cargar_asset('assets/vaca.png')
oveja_image = cargar_asset('assets/oveja.png')

#// La carga de sonido se ha desactivado para esta versión.
#// collision_sound = pygame.mixer.Sound('assets/sonido.wav')

#* Preparando la lista de animales para el juego
animals = []
animal_images = [img for img in [pig_image, dog_image, vaca_image, oveja_image] if img is not None]

if not animal_images:
    #! ADVERTENCIA: No se cargó ninguna imagen de animal. El juego funcionará pero no aparecerán objetivos.
    print("! ADVERTENCIA: No se cargó ninguna imagen de animal. No aparecerán objetivos.")

for _ in range(20):
    if animal_images:
        animals.append({
            "image": random.choice(animal_images),
            "pos": [random.randint(0, width - 50), random.randint(0, height - 50)]
        })

#* =================================================================================
#* DEFINICIÓN DE FUNCIONES PRINCIPALES
#* =================================================================================

def move_player(dx, dy):
    """
    * Mueve al jugador y lo mantiene dentro de los límites de la pantalla.
    * @param dx: Movimiento en el eje X (-1 para izquierda, 1 para derecha).
    * @param dy: Movimiento en el eje Y (-1 para arriba, 1 para abajo).
    """
    global player_x, player_y
    player_x += dx * speed
    player_y += dy * speed
    # Limita la posición para que el jugador no se salga de la pantalla
    player_x = max(0, min(player_x, width - 90))
    player_y = max(0, min(player_y, height - 100))

def check_collision():
    """
    * Verifica si el jugador ha colisionado con alguno de los animales.
    * Si hay colisión, elimina al animal de la lista.
    """
    global animals
    player_rect = pygame.Rect(player_x, player_y, 90, 100)
    for animal in animals[:]:
        animal_rect = pygame.Rect(animal["pos"][0], animal["pos"][1], 50, 50)
        if player_rect.colliderect(animal_rect):
            #// No se reproduce sonido en esta versión.
            #// collision_sound.play()
            animals.remove(animal)

def display_timer(screen, start_time):
    """
    * Dibuja el temporizador en la esquina superior izquierda de la pantalla.
    * @param screen: La superficie de Pygame donde se dibujará.
    * @param start_time: El tiempo de inicio del juego.
    """
    elapsed_time = int(time.time() - start_time)
    font = pygame.font.Font(None, 36)
    text = font.render(f"Tiempo: {elapsed_time}", True, black)
    screen.blit(text, (10, 10))

#* =================================================================================
#* BUCLE PRINCIPAL DEL JUEGO
#* =================================================================================
running = True
start_time = time.time()
while running:
    #* Manejo de eventos (ej. cerrar la ventana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #* Detección de teclas presionadas para el control del jugador
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:  dx = -1
    if keys[pygame.K_RIGHT]: dx = 1
    if keys[pygame.K_UP]:    dy = -1
    if keys[pygame.K_DOWN]:  dy = 1
    
    #* Mover al jugador si se presionó alguna tecla de dirección
    if dx != 0 or dy != 0:
        move_player(dx, dy)

    #* -----------------------------------------------------------------------------
    #* Sección de renderizado (dibujar todo en la pantalla)
    #* -----------------------------------------------------------------------------

    # 1. Limpiar la pantalla con un fondo blanco
    screen.fill(white)

    # 2. Dibujar todos los animales en sus posiciones
    for animal in animals:
        screen.blit(animal["image"], animal["pos"])
    
    # 3. Dibujar al jugador (solo si su imagen se cargó correctamente)
    if player_image:
        screen.blit(player_image, (player_x, player_y))
    
    # 4. Verificar colisiones y actualizar la lista de animales
    check_collision()

    # 5. Dibujar el temporizador
    display_timer(screen, start_time)

    # 6. Actualizar toda la pantalla para mostrar los cambios
    pygame.display.flip()
    
    #* Limitar el juego a 60 fotogramas por segundo (FPS)
    clock.tick(60)

#* =================================================================================
#* FINALIZACIÓN DEL PROGRAMA
#* =================================================================================
pygame.quit()
print("Juego finalizado. ¡Gracias por jugar!")
