import math
import pygame.display
import roads_use
import car_methods_repulsion as repulse
import time
import car_methods as algo
import data_export_method as exports

red = (255, 0, 0)
green = (0, 255, 0)

# leader = repulse.first_car(8, 8)
# follower = repulse.vehicle(0, 0, repulse.sedan)
# cars = [leader, follower]
#
# for step in range(100):  # using car_methods_repurlse
#     for i in range(len(cars) - 1, 0, -1):
#         print(step)
#         repulse.movement_vel_update(cars, 0.02)
#         print(str(cars[i].current_speed) + ' vel')
#         print(str(cars[i].current_location) + ' location')
#         print(str(cars[i-1].current_location) + ' leader car loc')
#
#         repulse.accel_calc(cars[i], cars[i - 1])
#         print(str(cars[i].acceleration) + ' accel')

first_vehicle = algo.first_car(6, 0, 10000)
following_vehicle2 = algo.car(6, 0, 0, 0, 400, 900, 80, 2, 0.1, 8, 16)
following_vehicle1 = algo.car(6, 0, 0, 0, 0, 900, 80, 2, 0.1, 8, 16)
vehicles = [first_vehicle, following_vehicle2, following_vehicle1]


def main_method():
    for step in range(6000):
        for i in range(len(vehicles) - 1, 0, -1):
            print(step)
            algo.desired_dist(vehicles[i], vehicles[i - 1])
            algo.IDM_accel(vehicles[i], vehicles[i - 1])
            algo.moving(vehicles, 0.1)
            roads_use.draw_box(vehicles[0].current_location / 100, green)
            for x in range(len(vehicles) - 1, 0, -1):
                roads_use.draw_box(vehicles[x].current_location / 100, red)
            pygame.display.update()
            roads_use.delete_box(vehicles[0].current_location / 100)
            for x in range(len(vehicles) - 1, 0, -1):
                roads_use.delete_box(vehicles[x].current_location / 100)
        exports.export(vehicles, step)



main_method()
roads_use.pygame.quit()


