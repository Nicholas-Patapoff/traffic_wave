import math


class first_car:
    def __init__(self, car_speed, current_location):
        self.current_speed = car_speed
        self.current_location = current_location
    acceleration = 0


class sedan:
    preferred_distance = 0


class vehicle:
    def __init__(self, current_speed, current_location, car_type):
        self.current_speed = current_speed
        self.current_location = current_location
        self.car_type = car_type
        self.preferred_distance = car_type.preferred_distance

    acceleration = 0


def movement_vel_update(car_list, step_size):
    for item in car_list:
        item.current_location += item.current_speed * step_size + item.acceleration * (1 / 2)  * (step_size ** 2)
        item.current_speed = item.current_speed + item.acceleration * step_size



def accel_calc(back_car, front_car):
    back_car.acceleration = (distance_between(back_car, front_car) - back_car.preferred_distance) ** 3


def distance_between(back_car, front_car):
    return front_car.current_location - back_car.current_location
