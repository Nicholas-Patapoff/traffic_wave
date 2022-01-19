import csv
import pandas as pd

# all of this is so fucked since I'm disabled at csv


def export(list, step):
    with open('test_data.csv', 'a', newline='') as csvfile:  # opens a new file and appends to it
        file_writer = csv.writer(csvfile, delimiter=',')
        data = [['Velocity', []], ['accel', []], ['time_step', []], ['location', []]]  # absolute garbage, how to
    # arrange csvs like
    #   car step vel acce loc
    #    1  1     x   y    z
    #    2  1     x   y    z
    #    3  1     x   y    z

        for item in list:
            data[0][1].append(item.current_speed)
            data[1][1].append(item.acceleration)
            data[2][1].append(step)
            data[3][1].append(item.current_location)

        file_writer.writerow(data)


def read_data(file):
    with open(file, 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        for rows in file_reader:
            print(rows)