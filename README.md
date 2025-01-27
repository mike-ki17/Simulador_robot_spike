# Simulador de Rutas para el Robot SPIKE de LEGO

Este proyecto ha sido desarrollado para hacer más eficiente la programación del robot SPIKE de LEGO utilizado en la competencia **FIRST LEGO League**. Consiste en un simulador programado en Python que permite crear y probar rutas de manera precisa y sencilla antes de implementarlas en el robot real.

## 🚀 Funcionalidades Principales

### 1. **Simulador Escalado**
- El tablero del simulador está completamente escalado para representar fielmente el tablero original de la competencia.
- Las líneas visibles en el simulador ofrecen mediciones en centímetros, facilitando la planificación precisa de rutas.

### 2. **Botones de Control**
- Interfaz con botones que permiten asignar direcciones al robot (avanzar, retroceder, girar, etc.).
- Cada movimiento se registra como parte de la ruta diseñada.

### 3. **Exportación a MicroPython**
- Al finalizar la creación de la ruta, el simulador genera automáticamente un código en **MicroPython**.
- Este código incluye todas las instrucciones necesarias para que el robot interprete y ejecute la ruta creada en el software.

![Imagen de salida de instrucciones](./src/readme_images/Captura%20desde%202025-01-27%2011-16-02.png)

### 4. **Funciones Preconfiguradas**
- El código exportado está diseñado para integrarse con funciones previamente cargadas en el robot SPIKE, optimizando la eficiencia del proceso.

---

## 📸 Imágenes del Simulador

### Tablero Escalado
Representación fiel del tablero de juego, mostrando las líneas de medición en centímetros, tomada de la pagina oficial.
[Visita el sitio oficial de FIRST LEGO LEANGUE](https://www.first-lego-league.org/en/2024-25-season/challenge-resources/robot-game)
![Imagen del Tablero](./src/readme_images/Captura%20desde%202025-01-26%2012-03-00.png)

### Vista del Software
Interfaz amigable con botones para diseñar rutas y exportar el código en MicroPython.

![Vista del Software](./src/readme_images/Captura%20desde%202025-01-27%2011-13-09.png)

---

## 🎯 Beneficios

- **Precisión:** La simulación escalada permite evitar errores comunes en la planificación de rutas.
- **Optimización:** Generación automatizada de código en MicroPython que ahorra tiempo en la programación manual.
- **Flexibilidad:** Compatible con las funciones personalizadas ya cargadas en el robot.

---

## 📂 Instalación y Uso

### Requisitos
- Python 3.x instalado en tu sistema.
- Librerías necesarias (se incluyen en el archivo `requirements.txt`).

### Pasos
1. Clona este repositorio:
   ```bash
   git clone https://github.com/mike-ki17/Simulador_robot_spike.git
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el simulador:
   ```bash
   python simulador.py
   ```

---

## 🤝 Contribuciones

¡Este proyecto está abierto a contribuciones! Si tienes ideas para mejorarlo o encuentras algún problema, no dudes en crear un *issue* o enviar un *pull request*.

---


## 🏆 Agradecimientos

- **FIRST LEGO League** por inspirar el desarrollo de herramientas que fomenten la innovación y el aprendizaje.
- La comunidad de Python por sus recursos y soporte continuo.
