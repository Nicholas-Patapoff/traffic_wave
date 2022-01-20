import pygame as pg
import random

def get_user_preferences():
    print('How many cars do you want running?')
    how_many = input()
    print('What kind of car - must be sedan')
    car_type = input()
    print('where should the starting car be?')
    starting_location = input()
    return [how_many, car_type, starting_location]

print(random.randint(0, 10000))