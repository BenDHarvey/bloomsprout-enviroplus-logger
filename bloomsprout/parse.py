#!/usr/bin/env python3
import time
from datetime import timezone
import datetime

script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("../../bloomsprout-proto/compiled/python")

import bloomsprout_proto_pb2

class BloomsproutParser:
    def parse_enviro_list_to_bloomsprout_object(self, enviro_readings):

        reading = bloomsprout_proto_pb2.Reading()

        reading.instrument = "enviro+"
        reading.deviceName = "sense-02" # TODO: Fix me
        reading.interval = "1s"
        reading.readingTakenAt = int(time.time())


        measurments = []
        for m in enviro_readings:
            m = reading.measurements.add()
            m.value = 1.1
            m.name = 1
            m.unit = 1

            d = {"Value": m['value'], "Unit": m["unit"], "Name": m["name"]}
            measurments.append(d)

        return reading
