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

def draw_box(location, color):
    pygame.gfxdraw.rectangle(window, (location, 300, 10, 10), color)


def delete_box(location):
    pygame.gfxdraw.rectangle(window, (location, 300, 10, 10), black)





