#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smbus2
import time

class Am2320sensor:
    am2320address = 0x5c

    def __init__(self, smbus_addr = 1):
        self.bus = smbus2.SMBus(smbus_addr)

    def setup(self):
        """
        AM2320センサーを初期化する
        """
        try:
            self.bus.write_i2c_block_data(self.am2320address, 0x00, [])
        except OSError as e:
            print(e)

        time.sleep(0.1)

    def read(self):
        """
        AM2320からセンサの値を読み取る
        """
        try:
            self.bus.write_i2c_block_data(self.am2320address, 0x03, [0x00, 0x04])
        except OSError as e:
            print(e)

        time.sleep(0.02)

        blocks = self.bus.read_i2c_block_data(self.am2320address, 0, 6)

        humidity = ((blocks[2] << 8) + blocks[3]) / 10.0
        temperature = ((blocks[4] << 8) + blocks[5]) / 10.0

        return {'temperature': temperature, 'humidity': humidity}


