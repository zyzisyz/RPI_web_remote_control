#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import time
import os
from .Raspi_BMP085 import BMP085
import eeml

DEBUG = 1
LOGGER = 1


# COSM variables. The API_KEY and FEED are specific to your COSM account and must be changed
#API_KEY = 'YOUR_API_KEY'
#FEED = YOUR_FEED_ID
API_KEY = 'P75Xsh3VcsN97y2prMzdU4j-tx2SAKxURXFVSDh1OXBmYz0g'
FEED = 76422


API_URL = '/v2/feeds/{feednum}.xml' .format(feednum=FEED)


while True:
    # Initialise the BMP085 and use STANDARD mode (default value)
    # bmp = BMP085(0x77, debug=True)
    bmp = BMP085(0x77)

    # To specify a different operating mode, uncomment one of the following:
    # bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode
    # bmp = BMP085(0x77, 1)  # STANDARD Mode
    # bmp = BMP085(0x77, 2)  # HIRES Mode
    # bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode

    temp = bmp.readTemperature()

    pressure = bmp.readPressure()

    altitude = bmp.readAltitude()

    if DEBUG:
        print("Temperature: %.2f C" % temp)
        print("Pressure:    %.2f hPa" % (pressure / 100.0))
        print("Altitude:    %.2f" % altitude)
        print()

    if LOGGER:
        # open up your cosm feed
        pac = eeml.Pachube(API_URL, API_KEY)

        # send light data
        pac.update([eeml.Data(0, ("%.2f" % temp), unit=eeml.Temperature())])

        # send light data
        pac.update(
            [eeml.Data(1, ("%.2f" % (pressure / 100.0)), unit=eeml.Pressure())])

        # send light data
        pac.update([eeml.Data(2, ("%.2f" % altitude), unit=eeml.Altitude())])

        # send data to cosm
        pac.put()

    # hang out and do nothing for 10 seconds, avoid flooding cosm
    time.sleep(30)
