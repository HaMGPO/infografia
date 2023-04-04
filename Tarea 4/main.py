from trabajo_clases import *
import arcade


# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Lineas con bresenham"



class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)
        self.pixel_size = 20

    def on_draw(self):
        arcade.start_render()

        points = get_line(30, 15, 5, 5)
        #self.draw_grid()
        #self.draw_line_points(points, arcade.color.AZURE_MIST)
        #self.draw_scaled_line(15, 15, 30, 30)
        self.draw_poligon([(20, 15), (10, 10), (15, 45)], [100, 255, 40, 150])
        self.poligono_aprox([[(15, 15), (16, 16), (17, 17), 
                              (18, 18), (19, 19), (20, 20), 
                              (21, 21), (22, 22), (23, 23), 
                              (24, 24), (25, 25), (26, 26), 
                              (27, 27), (28, 28), (29, 29), 
                              (30, 30)], 
                              [(30, 30), (29, 31), (28, 32), 
                               (27, 33), (26, 34), (25, 35), 
                               (24, 36), (23, 37), (22, 38), 
                               (21, 39), (20, 40), (19, 41), 
                               (18, 42), (17, 43), (16, 44), 
                               (15, 45)], 
                               [(15, 45), (15, 44), (15, 43), 
                                (15, 42), (15, 41), (15, 40), 
                                (15, 39), (15, 38), (15, 37), 
                                (15, 36), (15, 35), (15, 34), 
                                (15, 33), (15, 32), (15, 31), 
                                (15, 30), (15, 29), (15, 28), 
                                (15, 27), (15, 26), (15, 25), 
                                (15, 24), (15, 23), (15, 22), 
                                (15, 21), (15, 20), (15, 19), 
                                (15, 18), (15, 17), (15, 16), 
                                (15, 15)]])


    def draw_grid(self):
        # lineas verticales
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2, 
                0, 
                v_l + self.pixel_size / 2, 
                SCREEN_HEIGHT, 
                arcade.color.DARK_GRAY
            )

        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0, 
                h_l + self.pixel_size / 2, 
                SCREEN_WIDTH, 
                h_l + self.pixel_size / 2, 
                arcade.color.LIGHT_GRAY
            )

    def draw_line_points(self, points,  color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)

    def draw_scaled_line(self, x0, y0, x1, y1, color):
        arcade.draw_line(
            x0 * self.pixel_size, 
            y0 * self.pixel_size, 
            x1 * self.pixel_size, 
            y1 * self.pixel_size,
            color,
            5
        )
    
    def draw_poligon(self, puntos, color): #unicamente armandolo con los puntos de los vertices
        max_index = len(puntos) - 1 
        

        for i in range(0, max_index):
            self.draw_scaled_line(puntos[i][0] ,
                            puntos[i][1], 
                            puntos[i+1][0], 
                            puntos[i+1][1], color)
            
        self.draw_scaled_line(puntos[max_index][0] ,
                            puntos[max_index][1], 
                            puntos[0][0], 
                            puntos[0][1], color)
        
    def poligono_aprox(self, aprox_pol): #dibujo con las aproximaciones producto de mi metodo poligon de trabajo_clases
        for i in aprox_pol:
            self.draw_poligon(i, [255, 255, 40, 150])          

if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()