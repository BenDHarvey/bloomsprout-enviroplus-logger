#!/usr/bin/env python3
import time

class BloomsproutParser:
    def parse_enviro_list_to_bloomsprout_object(self, enviro_readings):
        now = time.time()

        measurments = []
        for m in enviro_readings:
            d = {"Value": m['value'], "Unit": m["unit"], "Name": m["name"]}
            measurments.append(d)

        meta = {"Instrument": "enviro+", "Id": "sense-02"}

        return {"Timestamp": now, "Measurments": measurments, "Meta": meta}
