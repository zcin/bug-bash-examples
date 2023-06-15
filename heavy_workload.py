import asyncio
from ray import serve

@serve.deployment
class Heavy:
    async def __call__(self):
        for _ in range(10):
            await asyncio.sleep(0.1)
        return "Hello"

app = Heavy.bind()
