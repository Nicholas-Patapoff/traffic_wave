import pygame.display
import time
import car_methods
import roads_use
import user_input as user
import car_methods as algo
import data_export_method as exports

draw_scale = 10  # scales how quickly cars are supposed to move across screen based on current location / x length scrn
box_scale = 5  # how many pixels for x and y axis cars are
red = (255, 0, 0)  # color according to RGB
green = (0, 255, 0)
white = (255, 255, 255)
user_settings = user.car_settings()
vehicles = []
vehicles = car_methods.sedan_creation(vehicles, user_settings[0], 5000)


def main_method():
    starting_time = time.time()
    step = 1
    while step:  # each step is for calculations
        current_time = time.time()
        if not user_settings[1] <= (current_time - starting_time):
            for i in range(len(vehicles) - 1, 0, -1):  # iterates through list of init. vehicles from last to first
                algo.desired_dist(vehicles[i], vehicles[i - 1])  # updates desired distances in the classes of the cars
                algo.IDM_accel(vehicles[i],
                               vehicles[i - 1])  # updates new accel based on the previously found desired dist
                algo.moving(vehicles,
                            0.1)  # moves the vehicles into new locations based on accel, velocity, and step size
                for x in range(len(vehicles) - 1, -1, -1):  # iterates all cars and draws boxes at loc
                    roads_use.draw_box(vehicles[x].current_location / draw_scale, roads_use.dynamic_color(vehicles[x]),
                                       box_scale)
                pygame.display.update()  # updates display
                for x in range(len(vehicles) - 1, -1, -1):  # deletes cars
                    roads_use.delete_box(vehicles[x].current_location / draw_scale, box_scale)
            exports.export_data(step, vehicles)  # exports location, vel, accel, time stamp loc into .txt
        elif user_settings[1] <= (current_time - starting_time):
            for i in range(len(vehicles) - 1, -1, -1):  # iterates through list of init. vehicles from last to first
                algo.desired_dist(vehicles[i], vehicles[i - 1])  # updates desired distances in the classes of the cars
                algo.IDM_accel(vehicles[i],
                               vehicles[i - 1])  # updates new accel based on the previously found desired dist
                algo.moving(vehicles,
                            0.1)  # moves the vehicles into new locations based on accel, velocity, and step size
                for x in range(len(vehicles) - 1, -1, -1):  # iterates all cars and draws boxes at loc
                    roads_use.draw_box(vehicles[x].current_location / draw_scale, roads_use.dynamic_color(vehicles[x]),
                                       box_scale)
                pygame.display.update()  # updates display
                for x in range(len(vehicles) - 1, -1, -1):  # deletes cars
                    roads_use.delete_box(vehicles[x].current_location / draw_scale, box_scale)
            exports.export_data(step, vehicles)  # exports location, vel, accel, time stamp loc into .txt
        if user_settings[2] <= (current_time - starting_time):
            return
        step += 1


main_method()
roads_use.pygame.quit()  # quits the window
exports.test_data.close()
