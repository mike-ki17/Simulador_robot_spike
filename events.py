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
            "derecha": False
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                eventos["teclas"]["arriba"] = True
            elif event.key == pygame.K_DOWN:
                eventos["teclas"]["abajo"] = True
            elif event.key == pygame.K_LEFT:
                eventos["teclas"]["izquierda"] = True
            elif event.key == pygame.K_RIGHT:
                eventos["teclas"]["derecha"] = True

    
    return eventos
