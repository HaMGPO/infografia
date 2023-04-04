import arcade

#Definicion de constantes 
SCREEN_WIDth = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Hola Arcade"

#Definicion de clase ventana
class Hola(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDth, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        #inicio renderizado
        arcade.start_render()

        #dibujar
        arcade.draw_triangle_filled(300 + 40, 300,
                               300, 300 - 100,
                               300 + 80, 300 - 100,
                               arcade.color.DARK_GREEN)

        arcade.draw_lrtb_rectangle_filled(300 + 30, 300 + 50, 300 - 100, 300 - 140,
                                     arcade.color.DARK_BROWN)

        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDth, 160, 0,
                                     arcade.color.GREEN)

if __name__ == "__main__": #Metodo main
    app = Hola()
    arcade.run() 