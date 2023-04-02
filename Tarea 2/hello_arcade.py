# importamos el paquete
import arcade
import math
import cmath
import random


# definicion de constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Hola Arcade"



def draw_flower():
    petal_number = 16
    final_angle = 360
    angle_step = final_angle // petal_number
    
    for angle in range(0, final_angle, angle_step):
        r = 70 + int(angle / 3)
        phi = math.radians(angle)
        center_c = cmath.rect(r, phi)
        arcade.draw_circle_filled(
            int(center_c.real + SCREEN_WIDTH / 2),
            int(center_c.imag + SCREEN_HEIGHT / 2),
            30,
            arcade.color.RED_ORANGE
        )
        arcade.draw_circle_outline(
            int(center_c.real + SCREEN_WIDTH / 2),
            int(center_c.imag + SCREEN_HEIGHT / 2),
            30,
            arcade.color.BLACK,
            10
        )

    arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 50, arcade.color.YELLOW)

def dibujar_elipse_color_random(center_x: float, center_y: float,
                          width: float, height: float,
                          num_segments: int = 128):
    COLORS = [arcade.color.BOTTLE_GREEN	, arcade.color.GREEN, arcade.color.BRIGHT_GREEN	, arcade.color.BRITISH_RACING_GREEN, arcade.color.BRUNSWICK_GREEN, arcade.color.BUD_GREEN]
    color = random.choice(COLORS)
    arcade.draw_ellipse_filled(center_x,
            center_y, 
            width, 
            height, 
            color, num_segments, -1)

def draw_leafs(petal_number, final_angle, start_angle):
        angle_step = final_angle // petal_number
        
        
        for angle in range(start_angle, final_angle+start_angle, angle_step):
            dibujar_elipse_color_random(int(SCREEN_WIDTH / 2),
                                         int(SCREEN_HEIGHT / 2), 
                                         final_angle / (petal_number), 
                                         360, 
                                         angle+angle_step)
  
        for angle in range(start_angle, final_angle+start_angle, angle_step):
            arcade.draw_ellipse_outline(int(SCREEN_WIDTH / 2),
                                         int(SCREEN_HEIGHT / 2), 
                                         final_angle / petal_number, 
                                         360, 
                                         arcade.color.BLACK, 10, angle+angle_step, -1)
        
        for angle in range(start_angle, final_angle+start_angle, angle_step):
            a = arcade.draw_ellipse_outline(int(SCREEN_WIDTH / 2),
                                         int(SCREEN_HEIGHT / 2), 
                                         10, 
                                         360, 
                                         arcade.color.BLACK, 10, angle+angle_step, -1)

    

if __name__ == "__main__":
    # Crear nueva ventana
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Cambiar el color de fondo
    arcade.set_background_color(arcade.color.WHITE)

    # iniciar render
    arcade.start_render()

    # Funciones para dibujar
    draw_leafs(5, 360, 45)

    # finalizar render
    arcade.finish_render()

    # Correr el programa
    arcade.run()
