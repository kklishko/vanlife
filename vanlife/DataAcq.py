"""
@title
@description
"""
import argparse
import csv
import os
import time

import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4


def log_sensor(sensor_data: dict, log_fname: str):
    save_dir = os.path.dirname(log_fname)
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

    file_exists = os.path.isfile(log_fname)
    open_mode = 'a+' if file_exists else 'w+'
    fieldnames = list(sensor_data.keys())
    with open(log_fname, mode=open_mode) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(sensor_data)
    return


def run_recorder(run_length: int, log_name: str, sleep_time: int = 1):
    start_time = time.time()
    while True:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print(f'Temp={temperature:0.2f}C  Humidity={humidity:0.2f}%')
            log_sensor({'humidity': humidity, 'temperature': temperature}, log_name)
        else:
            print('Sensor failure. Check wiring.')
        curr_time = time.time()
        d_time = curr_time - start_time
        if 0 < run_length <= d_time:
            break
        time.sleep(sleep_time)
    return


class DataAcq:

    def __init__(self):
        return


def main(main_args):
    record_length = main_args.get('record_length', False)
    data_fname = main_args.get('data_file', '')

    run_recorder(record_length, data_fname)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--record_length', type=int, nargs=1, default=-1,
                        help='')
    parser.add_argument('--data_file', type=str, nargs=1, default='',
                        help='')

    args = parser.parse_args()
    main(vars(args))
