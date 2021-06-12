#!/usr/bin/env python3
import asyncio
import time
import logging
from threading import Thread
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

class NatsPublisher:

    def __init__(self, loop):
        logging.info("Init the nats logger")

        self.nc = NATS()
        self.loop = loop

        self.options = {
            "loop": loop,
            "error_cb": self.error_cb,
            "closed_cb": self.closed_cb,
            "reconnected_cb": self.reconnected_cb,
            "servers": ["nats://dev-k3s-1:4222"]
        }

    async def error_cb(self, e):
        print("Error:", e)

    async def closed_cb(self):
        print("Connection to NATS is closed.")

    async def reconnected_cb(self):
        print(f"Connected to NATS at {nc.connected_url.netloc}...")


    async def publish(self, subject, data):
        logging.info(f"Publishing on {subject}")
        await self.nc.publish(subject, data.encode())

    async def connect(self):
        logging.info(f"connecting to nats server")
        await self.nc.connect(**self.options)
