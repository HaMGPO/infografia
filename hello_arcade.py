#importacion de paquetes
import arcade 

#definicion de contantes (Con mayusculas)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Hola Arcade"

#Creamos una ventana
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

#Cambiamos el color de fondo
arcade.set_background_color(arcade.color.WHITE)

#comenzamos a rendereizar (mostrar lo dibujado)
arcade.start_render()

#Funciones de dibujado

arcade.draw_triangle_filled(300 + 40, 300,
                               300, 300 - 100,
                               300 + 80, 300 - 100,
                               arcade.color.DARK_GREEN)

arcade.draw_lrtb_rectangle_filled(300 + 30, 300 + 50, 300 - 100, 300 - 140,
                                     arcade.color.DARK_BROWN)

arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 160, 0,
                                     arcade.color.GREEN)

#finalizamos el renderizado (terminados de graficar lo dibujado)
arcade.finish_render()

#Ejecucion del programa
arcade.run()