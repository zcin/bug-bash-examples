import ray
from ray import serve
import os

@serve.deployment
class MyModel:
    def __init__(self):
        pass

    def __call__(self):
        content = ""
        with open("file.txt") as f:
            content = f.read()
        return content

app = MyModel.bind()
