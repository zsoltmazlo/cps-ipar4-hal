#!/usr/bin/python
#---------------------------------------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#           bh1750.py
# Read data from a BH1750 digital light sensor.
#
# Author : Matt Hawkins
# Date   : 26/06/2018
#
# For more information please visit :
# https://www.raspberrypi-spy.co.uk/?s=bh1750
#
#---------------------------------------------------------------------
import smbus
import time

# Define some constants from the datasheet


class BH1750:
    ADDRESS     = 0x23 # Default device I2C address
    POWER_DOWN  = 0x00 # No active state
    POWER_ON    = 0x01 # Power on
    RESET       = 0x07 # Reset data register value

    # Start measurement at 4lx resolution. Time typically 16ms.
    CONTINUOUS_LOW_RES_MODE = 0x13
    # Start measurement at 1lx resolution. Time typically 120ms
    CONTINUOUS_HIGH_RES_MODE_1 = 0x10
    # Start measurement at 0.5lx resolution. Time typically 120ms
    CONTINUOUS_HIGH_RES_MODE_2 = 0x11
    # Start measurement at 1lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_HIGH_RES_MODE_1 = 0x20
    # Start measurement at 0.5lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_HIGH_RES_MODE_2 = 0x21
    # Start measurement at 1lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_LOW_RES_MODE = 0x23


    def __init__(self, address=ADDRESS):
        self.address = address
        self.bus = smbus.SMBus(1)  # Rev 2 Pi uses 1


    def __convert_data_to_number(self, data):
      # Simple function to convert 2 bytes of data
      # into a decimal number. Optional parameter 'decimals'
      # will round to specified number of decimal places.
      result=(data[1] + (256 * data[0])) / 1.2
      return (result)

    def read_intensity(self):
      # Read data from I2C interface
      try:
        data = self.bus.read_i2c_block_data(self.address, self.CONTINUOUS_LOW_RES_MODE)
        return True, self.__convert_data_to_number(data)
      except OSError:
        print("Error during reading light intensity from BH1750")
      return False, 0
