import pygame

def exportacion_archivos ():
    src = {
        "Tablero" : pygame.image.load("./src/img/FLL_Challenge_2024-25_Robot-Game_Spielfeldmatte_mit_Modellen(1).png"),
        "Robot" : pygame.image.load("./src/img/robot_spike.png"),
        "Btn_borrar" : pygame.image.load("./src/img/btn_back.png"),
        "Btn_avanzar" : pygame.image.load("./src/img/avanza.png"),
        "Btn_retroceder" : pygame.image.load("./src/img/retrocede.png"),
        "Btn_giro_derecha" : pygame.image.load("./src/img/derecha.png"),
        "Btn_giro_izquierda" : pygame.image.load("./src/img/izquierda.png"),
        "Run" : pygame.image.load("./src/img/run.png"),
    }

    return src
