from __future__ import annotations

import asyncio
from pathlib import Path
import time

from farm_ng.canbus.canbus_pb2 import Twist2d
from farm_ng.core.event_client import EventClient
from farm_ng.core.event_service_pb2 import EventServiceConfig
from farm_ng.core.events_file_reader import proto_from_json_file

LINEAR_VELOCITY = 0.1
ACC = 0.05
ANGULAR_VELOCITY = 0.05
DISTANCE = 0.30 # in m
TIME_REQ = (DISTANCE/LINEAR_VELOCITY) - 0.1

class Motors():
    def __init__(self, file_path="common/service_config.json"):
        service_config_path = Path(file_path)
        self.twist = Twist2d()
        config: EventServiceConfig = proto_from_json_file(service_config_path, EventServiceConfig())
        self.client: EventClient = EventClient(config)

    async def move_motors(self, speeds) -> None:
        for speed in speeds:
            self.twist.linear_velocity_x = speed
            if abs(speed) == LINEAR_VELOCITY: treq = TIME_REQ
            else: treq = 0.01
            st = time.time()
            while time.time()-st < treq:
                await self.client.request_reply("/twist", self.twist)
                await asyncio.sleep(0.05)
    
    async def forward(self) -> None:
        fspeeds = [ACC, LINEAR_VELOCITY, ACC, 0]
        await self.move_motors(fspeeds)

    async def reverse(self) -> None:
        rspeeds = [-ACC, -LINEAR_VELOCITY, -ACC, 0]
        await self.move_motors(rspeeds)
