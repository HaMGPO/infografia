import arcade
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SQUARE_SIZE = 50
GRID_WIDTH = SCREEN_WIDTH // SQUARE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // SQUARE_SIZE
COLORS = [arcade.color.RED, arcade.color.GREEN, arcade.color.BLUE, arcade.color.YELLOW]

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Cuadrícula de cuadrados")
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        for row in range(GRID_HEIGHT):
            for column in range(GRID_WIDTH):
                x = column * SQUARE_SIZE + SQUARE_SIZE // 2
                y = row * SQUARE_SIZE + SQUARE_SIZE // 2
                color = random.choice(COLORS)
                arcade.draw_rectangle_filled(x, y, SQUARE_SIZE, SQUARE_SIZE, color)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
