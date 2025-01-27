import pygame

def manejar_eventos():
    """
    Gestiona los eventos del juego (teclado, ratón, cierre de ventana, etc.)
    Devuelve el estado de los eventos y las acciones.
    """
    eventos = {
        "salir": False,
        "click": [False, 0],
        "manejador_click": False
    }
    
    # Obtener todos los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            eventos["salir"] = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            eventos["click"] = [True, event.pos]  # Detectar clic en el botón
        elif event.type == pygame.MOUSEBUTTONUP:
            eventos["manejador_click"] = True
    
    return eventos
