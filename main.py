#!/usr/bin/env python3
import time
import asyncio
import logging
import json
import os
from threading import Thread
from nats_publisher import nats_publisher
from enviro import environ
from bloomsprout import parse

logging.basicConfig(
    format="%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

async def run(loop):
    logging.info("starting environplus logger")

    c = nats_publisher.NatsPublisher(loop)
    en = environ.Enviro()
    bp = parse.BloomsproutParser()

    data = en.display_and_return_readings()

    await c.connect()

    while True:
        data = en.display_and_return_readings()
        proto_data = bp.parse_enviro_list_to_bloomsprout_object(data)

        # make into proto btyes and then pass to nats for transmission
        json_data = json.dumps(parsed_data)
        await asyncio.sleep(1)

        await c.publish("metrics_test", json_data)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run(loop))
    finally:
        loop.close()
