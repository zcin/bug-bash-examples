import time
from ray import serve

@serve.deployment
class Heavy:
    def __call__(self):
        time.sleep(3)
        return "Hello"

app = Heavy.bind()
