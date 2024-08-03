# импорты библиотек
import main
from graphlern import Pixel, Message


# объявление переменных(констант)
GRID_WIDTH = 10
GRID_HEIGHT = 10
PIXEL_SIZE = 50
BACKGROUND_COLOR = "#ffeba1"
SOUND = ""


# Цвет смайла:  #030418

# координаты x пикселей смайла

x_coords_when_y_equals_2 = []
x_coords_when_y_equals_3 = []
x_coords_when_y_equals_7 = []
x_coords_when_y_equals_8 = []


# отрисовка
def draw(window):
    # Здесь пиши свой код
    
    Pixel(window, x=1, y=2, color="#030418", size=PIXEL_SIZE)
