import pygame
import time
from pygame import gfxdraw

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
rectangle = (0, 10, 40, 0)

pygame.init()
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Window')


def draw_box(location, color, box_size):
    pygame.gfxdraw.rectangle(window, (location, 300, box_size, box_size), color)


def delete_box(location, box_size):
    pygame.gfxdraw.rectangle(window, (location, 300, box_size, box_size), black)


def dynamic_color(car):
    if car.current_speed < 0:
        r = 255
        g = 0
    elif car.current_speed > 255:
        r = 0
        g = 255
    else:
        r = (1 - car.current_speed / car.max_speed) * 255
        g = 255 * car.current_speed / car.max_speed
    color = (r, g, 0)
    return color
