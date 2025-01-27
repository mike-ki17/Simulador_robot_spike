import pygame
import math
from source import exportacion_archivos
from events import manejar_eventos

# Inicializar Pygame
pygame.init()

# Archivos estaticos
image = exportacion_archivos()

'''
******************************
** Asignación de elementos ***
******************************
'''
tablero = image['Tablero']
robot = image['Robot']
btn_borrar = image['Btn_borrar']
btn_avanzar = image['Btn_avanzar']
btn_retroceder = image['Btn_retroceder']
btn_giro_derecho = image['Btn_giro_derecha']
btn_giro_izquierdo = image['Btn_giro_izquierda']
run = image['Run']

'''
******************************
*** Dimescionamiento de    ***
*** elementos              ***
******************************
'''
# Tamaño ventana = tamaño del tablero
screen_width, screen_height = tablero.get_size()
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Tablero Juego del robot ")

# Obtener las dimensiones de la imagen (opcional, para centrarla)
image_rect = tablero.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2)

robot_rect = robot.get_rect()
robot_rect.topleft = (100, 100)

btn_borrar_rect = btn_borrar.get_rect()
btn_borrar_rect.topleft = (800, 0) 

btn_avanzar_rect = btn_avanzar.get_rect()
btn_avanzar_rect.topleft = (800, 70)

btn_retroceder_rect = btn_retroceder.get_rect()
btn_retroceder_rect.topleft = (800, 150)

btn_giro_derecho_rect = btn_giro_derecho.get_rect()
btn_giro_derecho_rect.topleft = (800, 230)

btn_giro_izquierdo_rect = btn_giro_izquierdo.get_rect()
btn_giro_izquierdo_rect.topleft = (800, 310)

run_rect = run.get_rect()
run_rect.center = (60, 70)

num_columns = 10
num_rows = 6  # Ajustado a 6 filas

# Calcular el tamaño de cada cuadrado
square_width = (screen_width-197) // num_columns 
square_height = (screen_height - 8) // num_rows

# Colores
border_color = (190, 0, 0)  # Color rojo para los bordes
background_color = (255, 255, 255)  # Fondo blanco

# Grosor del borde
border_thickness = 1

# Cargar una imagen
# Asegúrate de tener una imagen en la misma carpeta, o ajusta la ruta

start_x = 100
start_y = -10

line_color = (0, 255, 0)  # Color verde para la línea
text_color = (255, 255, 255)  # Color negro para el texto

# Fuente para mostrar la longitud
font = pygame.font.SysFont("Arial", 24)

# Variables para el inicio de la línea
start_pos = None


# Lista para guardar las líneas dibujadas
lines = []

button_clicked = False
# Se almacena el recorrido para el robot
recorrido = []

# Funcion para convertir pixeles a centimetros
pixels_to_cm = lambda px: ((px/300) * 2.54) * 33.7

def borrar_elemtos_array(array):
    if array:  # Verificar si la lista no está vacía
        array.pop()
show_secundary_window = False

recorrido_export = ''


# Loop principal
running = True
while running:
    # Manejar eventos
    eventos = manejar_eventos()
    '''
    ******************************
    *** Manejadores de eventos ***
    ******************************
    '''
    if eventos['salir']:
        running = False
    
    if eventos['click'][0]:
        if btn_borrar_rect.collidepoint(eventos['click'][1]) and not button_clicked:
            borrar_elemtos_array(lines)  # Borrar la última línea
            borrar_elemtos_array(lines) 
            borrar_elemtos_array(recorrido)
            button_clicked = True  # Marcar que el botón ha sido clickeado
        
        if btn_avanzar_rect.collidepoint(eventos['click'][1])and not button_clicked:
            recorrido.append(['avanzar', round(pixels_to_cm(length))])
            recorrido_export += f'\nawait Mover({round(pixels_to_cm(length))})'
        
        if btn_retroceder_rect.collidepoint(eventos['click'][1])and not button_clicked:
            recorrido.append(['retroceder', round(pixels_to_cm(length))])
            recorrido_export += f'\nawait Mover({-(round(pixels_to_cm(length)))})'

        if btn_giro_derecho_rect.collidepoint(eventos['click'][1])and not button_clicked:
            recorrido.append(['giro_derecho', round(pixels_to_cm(length))])
            recorrido_export += "\nawait Girar('derecha')"
        
        if btn_giro_izquierdo_rect.collidepoint(eventos['click'][1])and not button_clicked:
            recorrido.append(['giro_izquierdo', round(pixels_to_cm(length))])
            recorrido_export += "\nawait Girar('izquierda')"

        if run_rect.collidepoint(eventos['click'][1]) and not button_clicked:
            print('Generando el codigo ....')
            print(recorrido_export)

    if eventos['manejador_click']:
        # Resetear la bandera después de que el mouse sea soltado
        if button_clicked:
            button_clicked = False


    # Dibujar la imagen en la pantalla
    screen.fill((0, 0, 0))  # Color de fondo (negro)
    screen.blit(tablero, image_rect)  # Dibujar la imagen
    screen.blit(btn_borrar, btn_borrar_rect.topleft)  # Dibujar el 
    screen.blit(btn_avanzar, btn_avanzar_rect.topleft)
    screen.blit(btn_retroceder, btn_retroceder_rect.topleft)
    screen.blit(btn_giro_derecho, btn_giro_derecho_rect.topleft)
    screen.blit(btn_giro_izquierdo, btn_giro_izquierdo_rect.topleft)
    screen.blit(run, run_rect)


    for row in range(num_rows):
        for col in range(num_columns):
            # Calcular la posición de cada cuadrado con el desplazamiento inicial
            x = start_x + col * square_width
            y = start_y + row * square_height
            # Dibujar el borde del cuadrado (sin relleno)
            pygame.draw.rect(screen, border_color, (x, y, square_width, square_height), border_thickness)


    for line in lines:
        pygame.draw.line(screen, line_color, line[0], line[1], 3)

    # Obtener la posición del mouse
    mouse_pos = pygame.mouse.get_pos()

    # Si se presiona el botón del mouse, empezar la línea
    if pygame.mouse.get_pressed()[0]:  # Botón izquierdo del mouse
        if start_pos is None:  # Si no hay un punto de inicio, lo establecemos
            start_pos = mouse_pos

        # Dibujar la línea desde el inicio hasta la posición actual del mouse
        pygame.draw.line(screen, line_color, start_pos, mouse_pos, 3)

        # Calcular la longitud de la línea
        dx = mouse_pos[0] - start_pos[0]
        dy = mouse_pos[1] - start_pos[1]
        length = math.sqrt(dx**2 + dy**2)

        # Mostrar la longitud en pantalla
        length_text = font.render(f"Longitud: {pixels_to_cm(length):.2f} CM", True, text_color)
        screen.blit(length_text, (10, 10))

    # Si no se está presionando el mouse, guardar la línea y reiniciar el inicio
    if not pygame.mouse.get_pressed()[0] and start_pos is not None:
        lines.append((start_pos, mouse_pos))
        start_pos = None


    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
