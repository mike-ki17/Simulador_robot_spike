import pygame

def manejar_eventos():
    """
    Gestiona los eventos del juego (teclado, ratón, cierre de ventana, etc.)
    Devuelve el estado de los eventos y las acciones.
    """
    eventos = {
        "salir": False,
        "click": [False, 0],
        "manejador_click": False,
        "teclas" : {
            "arriba": False,
            "abajo": False,
            "izquierda": False,
            "derecha": False,
            "r": False,
            "e": False
        }
    }
    
    # Obtener todos los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            eventos["salir"] = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            eventos["click"] = [True, event.pos]  # Detectar clic en el botón
        elif event.type == pygame.MOUSEBUTTONUP:
            eventos["manejador_click"] = True
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            estado = event.type == pygame.KEYDOWN  # True si se presiona, False si se suelta
            if event.key == pygame.K_UP:
                eventos["teclas"]["arriba"] = estado
            elif event.key == pygame.K_DOWN:
                eventos["teclas"]["abajo"] = estado
            elif event.key == pygame.K_LEFT:
                eventos["teclas"]["izquierda"] = estado
            elif event.key == pygame.K_RIGHT:
                eventos["teclas"]["derecha"] = estado
            elif event.key == pygame.K_r:
                eventos['teclas']['r'] = estado
            elif event.key == pygame.K_e:
                eventos['teclas']['e'] = estado


    
    return eventos
