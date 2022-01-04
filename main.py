import math
import pygame.display
import roads_use
import car_methods_repulsion as repulse
import time
import car_methods as algo

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

first_vehicle = algo.first_car(6, 60, 5000)
following_vehicle = algo.car(6, 0, 0, 0, 0, 900, 80, 2, 0.1, 8, 16)

vehicles = [first_vehicle, following_vehicle]


def main_method():
    for step in range(9000):
        for i in range(len(vehicles) - 1, 0, -1):
            print(step)
            algo.desired_dist(vehicles[i], vehicles[ i - 1])
            algo.IDM_accel(vehicles[i], vehicles[i - 1])
            algo.moving(vehicles, 0.1)
            roads_use.draw_box(vehicles[i].current_location / 100, red)
            roads_use.draw_box(vehicles[i - 1].current_location / 100, green)
            pygame.display.update()
            roads_use.delete_box(vehicles[i].current_location / 100)
            roads_use.delete_box(vehicles[i - 1].current_location / 100)


main_method()
roads_use.pygame.quit()


