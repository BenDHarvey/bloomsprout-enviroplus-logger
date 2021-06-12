#!/usr/bin/env python3
import time
import asyncio
import logging
from threading import Thread
from nats_publisher import nats_publisher
from enviro import environ

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

async def run(loop):
    logging.info("Running program...")

#    c = nats_publisher.NatsPublisher(loop)
    en = environ.Enviro()

    data = en.display_and_return_readings()

#    await c.connect()
#
    while True:
#        await c.publish("test", "something")

        data = en.display_and_return_readings()
        await asyncio.sleep(1)

        print("THIS IS THE DATA: ", data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run(loop))
    finally:
        loop.close()
