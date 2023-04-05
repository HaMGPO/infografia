import arcade 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "lineas de bresenham"

class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.px = SCREEN_WIDTH / 2
        self.py = SCREEN_HEIGHT / 2
        self.movement = 5
        self.points = []

    def player_is_on_food(self): #Ya tengo los datos en mi clase
        """Funcion que detecta sie l jugador ha colisionado con un punto
        Devuelve el indice del punto en la lista self.points si existe 
        una colision, caso contrario devuelve -1
        """
        for index in range(0, len(self.points)):
            #print(index)
            mismo_x = False
            mismo_y = False
            if (self.points[index][0] + 5) >= self.px >= (self.points[index][0] - 5):
                mismo_x = True
            if (self.points[index][1] + 5) >= self.py >=  (self.points[index][1] - 5):
                mismo_y = True
            #print(mismo_x, mismo_y)
            if mismo_x and mismo_y:
                mismo_x = False
                mismo_y = False
                #print("reset")
                return index
        return -1

    def on_key_press(self, symbol:int, modifiers: int): #Detectar teclas presionadas
        #Symbol es la tecla presionada
        #modifiers: modificadores presionados

        if symbol == arcade.key.UP:
            self.py += self.movement
        if symbol == arcade.key.DOWN:
            self.py -= self.movement
        if symbol == arcade.key.LEFT:
            self.px -= self.movement
        if symbol == arcade.key.RIGHT:
            self.px += self.movement
    
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int): #Detectar clicks realizados
        """
            x: coordinada x del click 
            y: coordenada y del click
            button: boton del mouse presionado
            modifiers: teclas modificadas 
        """
        print(x, y, button)
        if button == arcade.MOUSE_BUTTON_LEFT:
            #print("Agregamdp punto en {}, {}".format(x, y))
            self.points.append((x, y))
    
    def on_update(self, delta_time: float): #Actualizar objetos de la app
       print(self.player_is_on_food())
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_point(self.px, self.py, arcade.color.RED, 5)
        if self.points: # Solo dibujara si hay puntos
            arcade.draw_points(self.points, arcade.color.GREEN, 5)
        arcade.draw_text(
            "Come todos los puntos verdes!",
            350,
            770,
            arcade.color.AERO_BLUE,
            15
        )

if __name__ == "__main__":
    ventana = App()
    arcade.run()