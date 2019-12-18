"""
@title
@description
"""
import argparse
import csv
import os
import time

import Adafruit_DHT

from vanlife import DATA_DIR

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4


def log_sensor(sensor_data: dict, log_fname: str):
    log_path = os.path.join(DATA_DIR, f'{log_fname}.csv')

    file_exists = os.path.isfile(log_path)
    open_mode = 'a+' if file_exists else 'w+'
    fieldnames = list(sensor_data.keys())
    with open(log_path, mode=open_mode) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(sensor_data)
    return


def run_recorder(run_length: int, log_name: str = None, sleep_time: int = 2):
    start_time = time.time()
    log_name = f'{log_name}_{int(start_time)}'
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        curr_time = time.time()

        if humidity is not None and temperature is not None:
            print(f'time: {curr_time} \t Temp={temperature:0.2f}C \t Humidity={humidity:0.2f}%')
            if log_name:
                log_sensor({'timestamp': time.time(), 'humidity': humidity, 'temperature': temperature}, log_name)
        else:
            print('Sensor failure. Check wiring.')

        d_time = curr_time - start_time
        if 0 < run_length <= d_time:
            break
        time.sleep(sleep_time)
    return


class DataAcq:

    def __init__(self):
        return


def main(main_args):
    record_length = main_args.get('record_length', -1)
    data_fname = main_args.get('data_file', None)
    delay = main_args.get('delay', 2)

    run_recorder(run_length=record_length, log_name=data_fname, sleep_time=delay)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--record_length', type=int, default=20,
                        help='')
    parser.add_argument('--data_file', type=str, default=None,
                        help='')
    parser.add_argument('--delay', type=int, default=2,
                        help='')

    args = parser.parse_args()
    main(vars(args))
