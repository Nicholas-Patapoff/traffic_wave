import time
import math
import numpy as np
import random


class car:  # car class which will be used to identify all the starting conditions
    def __init__(self, car_length, starting_speed, current_speed, starting_time, current_location, min_desired_dist,
                 max_speed, smoothness_accel, reaction_time, max_accel, min_accel):
        self.car_length = car_length  # units of meters
        self.starting_time = starting_time
        self.current_speed = current_speed
        self.starting_speed = starting_speed
        self.current_location = current_location
        self.min_desired_dist = min_desired_dist
        self.max_speed = max_speed
        self.smoothness_accel = smoothness_accel
        self.reaction_time = reaction_time
        self.max_accel = max_accel
        self.min_accel = min_accel
        self.back_location = self.current_location - self.car_length / 2
        self.front_location = self.current_location + self.car_length / 2
    acceleration = 0
    desired_dist = 0
    all_location_times = {}

def sedan_creation(list, number, starting_location):

    list.append(car(6, 0, 0, 0, starting_location, 200, 80, 2, 0.01, 16, 16))
    for i in range(number):
        list.append(car(6, 0, 0, 0, (200 * number - i * 200), 200, 80, 2, 0.01, 16, 16))
    return list

def IDM_accel(vehicle, leader):  # calculates acceleration
    vehicle.acceleration = vehicle.max_accel * (
            1 - ((vehicle.current_speed / vehicle.max_speed) ** vehicle.smoothness_accel) - \
            ((vehicle.desired_dist / actual_distances(leader, vehicle)) ** 2))


def desired_dist(vehicle, first_car):  # cacluates the new desired position of car based on currernt conditions
    vehicle.desired_dist = vehicle.min_desired_dist + \
                        (vehicle.reaction_time * vehicle.current_speed) + \
                        ((vehicle.current_speed * difference_in_speed(first_car, vehicle.current_speed)) /
                         math.sqrt(2 * vehicle.max_accel * vehicle.min_accel))


def moving(car_class_list, seconds_per_step):  # assign the cars new positions based on accel, vel, step size
    for vehicle in car_class_list:
        vehicle.current_location += move_from_accel(vehicle, seconds_per_step)
        vehicle.current_speed = new_velocity(vehicle, seconds_per_step)


def move_from_accel(vehicle, step_size):  # calculates movement using a kinematic eq
    distance_moved = vehicle.current_speed * step_size + (1 / 2) * vehicle.acceleration * (step_size ** 2)
    return distance_moved


def new_velocity(vehicle, seconds_per_step):  # finds new velocity based on accel
    return vehicle.current_speed + vehicle.acceleration * seconds_per_step


def actual_distances(leader, follower):  # finds the distance between a leading and a following car
    return leader.current_location - follower.current_location


def difference_in_speed(leader_class, follower_data):  # calulates differences in speed between leading and following
    return math.fabs(leader_class.current_speed - follower_data)

