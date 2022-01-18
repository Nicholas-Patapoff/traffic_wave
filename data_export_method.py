import csv
import pandas as pd


def export(list, step):
    with open('test_data.csv', 'a', newline='') as csvfile:
        file_writer = csv.writer(csvfile, delimiter=',')
        data = [['Velocity', []], ['accel', []], ['time_step', []], ['location', []]]

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