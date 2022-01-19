import pygame
import time
from pygame import gfxdraw

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)


pygame.init()  # inits pygame graphics
window = pygame.display.set_mode((1000, 600))  # makes a window of the specified size
pygame.display.set_caption('Window')  # names the window


def draw_box(location, color, box_size):  # function for drawing a box
    pygame.gfxdraw.rectangle(window, (location, 300, box_size, box_size), color)


def delete_box(location, box_size):  # function for deleting a box
    pygame.gfxdraw.rectangle(window, (location, 300, box_size, box_size), black)


def dynamic_color(car):  # dynamic car colors based on current velocity, moves from red to green as speed increases
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
