import math
import pygame.display
import roads_use
import car_methods_repulsion as repulse
import time
import car_methods as algo
import data_export_method as exports
draw_scale = 40
box_scale = 10
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

first_vehicle = algo.first_car(6, 30, 10000)
following_vehicle2 = algo.car(6, 0, 0, 0, 400, 200, 80, 2, 0.1, 8, 16)
following_vehicle1 = algo.car(6, 0, 0, 0, 0, 200, 80, 2, 0.1, 8, 16)
vehicles = [first_vehicle, following_vehicle2, following_vehicle1]


def main_method():
    for step in range(2000):
        for i in range(len(vehicles) - 1, 0, -1):
            print(step)
            algo.desired_dist(vehicles[i], vehicles[i - 1])
            algo.IDM_accel(vehicles[i], vehicles[i - 1])
            algo.moving(vehicles, 0.1)
            roads_use.draw_box(vehicles[0].current_location / draw_scale, white, box_scale)
            for x in range(len(vehicles) - 1, 0, -1):
                roads_use.draw_box(vehicles[x].current_location / draw_scale, roads_use.dynamic_color(vehicles[x]), box_scale)
            pygame.display.update()
            roads_use.delete_box(vehicles[0].current_location / draw_scale, box_scale)
            for x in range(len(vehicles) - 1, 0, -1):
                roads_use.delete_box(vehicles[x].current_location / draw_scale, box_scale)
        exports.export(vehicles, step)


main_method()
roads_use.pygame.quit()


