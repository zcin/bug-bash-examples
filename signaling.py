import asyncio
from ray import serve
from ray.serve.drivers import DAGDriver
from ray.serve.http_adapters import json_request

@serve.deployment(ray_actor_options={"num_cpus": 0})
class SignalDeployment:
    def __init__(self):
        self.ready_event = asyncio.Event()

    def __call__(self, clear = False):
        self.ready_event.set()
        if clear:
            self.ready_event.clear()

    async def wait(self):
        await self.ready_event.wait()

app = DAGDriver.bind(SignalDeployment.bind(), http_adapter=json_request)