import arcade
import random
import time
from hello_arcade import *




# definicion de constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Hola Arcade"

SQUARE_SIZE = 50
GRID_WIDTH = SCREEN_WIDTH // SQUARE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // SQUARE_SIZE
COLORS = [arcade.color.RED, arcade.color.WHITE, arcade.color.BLUE, arcade.color.YELLOW]

# Definicion de clase ventana
class Hola(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        # iniciar renderizado
        #self.start_render(5, 360, 45)

        # dibujar
        draw_flower()

    def start_render(self):
        arcade.start_render()
        for row in range(GRID_HEIGHT):
            for column in range(GRID_WIDTH):
                x = column * SQUARE_SIZE + SQUARE_SIZE // 2
                y = row * SQUARE_SIZE + SQUARE_SIZE // 2
                color = random.choice(COLORS)
                arcade.draw_rectangle_filled(x, y, SQUARE_SIZE, SQUARE_SIZE, color)

    

class Adios(Hola):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        self.start_render(5, 360)
        draw_flower()
    
    def start_render(self, petal_number, final_angle):
        super().start_render()
        for angle in range(0, 360, 165):
            draw_leafs(petal_number, final_angle, angle)


        
# entrypoint
if __name__ == "__main__":
    app = Adios()
 
    arcade.run()