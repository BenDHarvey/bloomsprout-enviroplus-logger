#!/usr/bin/env python3
import time
from datetime import timezone
import datetime

class BloomsproutParser:
    def parse_enviro_list_to_bloomsprout_object(self, enviro_readings):
        dt = datetime.datetime.now(timezone.utc)

        utc_time = dt.replace(tzinfo=timezone.utc)
        utc_timestamp = utc_time.timestamp()

        #x = utc_timestamp.split(".")
        x_string = str(utc_timestamp)

        x_split = x_string.split(".")

        measurments = []
        for m in enviro_readings:
            d = {"Value": m['value'], "Unit": m["unit"], "Name": m["name"]}
            measurments.append(d)

        meta = {"Instrument": "enviro+", "Id": "sense-02"}

        return {"Timestamp": int(x_split[0]), "Measurments": measurments, "Meta": meta}
