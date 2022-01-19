import pygame.display
import roads_use
import car_methods as algo
import data_export_method as exports
draw_scale = 40  # scales how quickly cars are supposed to move across screen based on current location / x length scrn
box_scale = 10  # how many pixels for x and y axis cars are
red = (255, 0, 0)  # color according to RGB
green = (0, 255, 0)
white = (255, 255, 255)

first_vehicle = algo.first_car(6, 60, 10000)  # leading car initialized with (length, speed, starting loc x axis screen)
following_vehicle2 = algo.car(6, 0, 0, 0, 0, 200, 80, 2, 0.1, 8, 16)  # following vehicle at dist 0
following_vehicle1 = algo.car(6, 0, 0, 0, 400, 200, 80, 2, 0.1, 8, 16)  # following vehicle at dist 400
vehicles = [first_vehicle, following_vehicle2, following_vehicle1]


def main_method():
    for step in range(2000):  # each step is for calculations
        for i in range(len(vehicles) - 1, 0, -1):  # iterates through list of init. vehicles from last to first
            algo.desired_dist(vehicles[i], vehicles[i - 1])  # updates desired distances in the classes of the cars
            algo.IDM_accel(vehicles[i], vehicles[i - 1])  # updates new accel based on the previously found desired dist
            algo.moving(vehicles, 0.1)  # moves the vehicles into new locations based on accel, velocity, and step size
            roads_use.draw_box(vehicles[0].current_location / draw_scale, white, box_scale)  # draws a box for
            # leading car, this is seperate from the rest for the sake of future adjustments to starting car
            for x in range(len(vehicles) - 1, 0, -1):  # iterates all other cars and draws boxes at loc
                roads_use.draw_box(vehicles[x].current_location / draw_scale, roads_use.dynamic_color(vehicles[x]), box_scale)
            pygame.display.update()  # updates display
            roads_use.delete_box(vehicles[0].current_location / draw_scale, box_scale)  # deletes front car
            for x in range(len(vehicles) - 1, 0, -1):  # deletes back cars
                roads_use.delete_box(vehicles[x].current_location / draw_scale, box_scale)
        exports.export_data(step, vehicles)  # exports location, vel, accel, time stamp loc into .txt


main_method()
roads_use.pygame.quit()  # quits the window
exports.test_data.close()

