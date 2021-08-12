#!/usr/bin/env python3
import time
import os
import logging
from datetime import timezone
import datetime

script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("../../bloomsprout-proto/compiled/python")

import bloomsprout_proto_pb2

logging.basicConfig(
    format="%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

class BloomsproutParser:
    def parse_unit_to_proto_enum(self, unit_string):
        '''
        Using the passed in string. Look for the matching enum value in the proto definition. Return the int for that definition value
        '''
        return_val = 0
        if unit_string is "C":
            return_val = 6
        elif unit_string is "hPa":
            return_val = 3
        elif unit_string is "%":
            return_val = 1
        elif unit_string is "Lux":
            return_val = 2
        elif unit_string is "kO":
            return_val = 4
        elif unit_string is "ug/m3":
            return_val = 5

        if return_val is 0:
            logging.info("[Warning] parse_name_to_proto_enum - return value is set to 0")

        return return_val

    def parse_name_to_proto_enum(self, unit_name_string):

        return_val = 0
        if unit_name_string is "temperature":
            return_val = 1
        elif unit_name_string is "pressure":
            return_val = 9
        elif unit_name_string is "humidity":
            return_val = 2
        elif unit_name_string is "oxidised":
            return_val = 5
        elif unit_name_string is "light":
            return_val = 3
        elif unit_name_string is "reduced":
            return_val = 10
        elif unit_name_string is "nh3":
            return_val = 4
        elif unit_name_string is "pm1":
            return_val = 6
        elif unit_name_string is "pm25":
            return_val = 8
        elif unit_name_string is "pm10":
            return_val = 7

        if return_val is 0:
            logging.info("[Warning] parse_name_to_proto_enum - return value is set to 0")


        return return_val


    def parse_enviro_list_to_bloomsprout_object(self, enviro_readings):

        reading = bloomsprout_proto_pb2.Reading()

        reading.instrument = "enviro+"
        reading.deviceName = "sense-02" # TODO: Fix me
        reading.interval = "1s"
        reading.readingTakenAt = int(time.time())


        measurments = []
        for m in enviro_readings:
            m = reading.measurements.add()
            m.value = m['value']
            m.name = parse_name_to_proto_enum(m["name"])
            m.unit = parse_unit_to_proto_enum(m["unit"])

            measurments.append(d)

        return reading
