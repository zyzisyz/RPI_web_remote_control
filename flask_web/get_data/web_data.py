#!python

import datetime


def get_date():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("time:", now)
    return now


def get_temperature():
    pass


def get_wet():
    pass


if __name__ == '__main__':
    print("time:", get_date())
    print("temperature:", get_temperature())
    print("wet:", get_wet())
