# импорты библиотек
import main
from graphlern import Pixel, Message


# объявление переменных(констант)
GRID_WIDTH = 10
GRID_HEIGHT = 10
PIXEL_SIZE = 50
BACKGROUND_COLOR = "#ffeba1"
SOUND = ""

 

# отрисовка
def draw(window):
    # Здесь пиши свой код

    # Пример рисования пикселя с помощью команды Pixel
    Pixel(window, x=6, y=7, color="green", size=PIXEL_SIZE)

            