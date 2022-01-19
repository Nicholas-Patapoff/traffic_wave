import pandas as pd
# write the column indicators

test_data = open('test_data.txt', 'a', newline='')

test_data.write("step car vel accel location")


def export_data(step, vehic):
    for i in range(len(vehic)):
        test_data.write("\n" + str(step) + ' ' + str(i) + ' ' + str(vehic[i].current_speed) + ' ' + str(vehic[i].acceleration) + ' ' + str(vehic[i].current_location))


