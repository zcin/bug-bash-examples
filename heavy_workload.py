import time
from ray import serve

@serve.deployment(
    autoscaling_config={
        "metrics_interval_s": 0.1,
        "min_replicas": 1,
        "max_replicas": 10,
        "look_back_period_s": 0.2,
        "downscale_delay_s": 0,
        "upscale_delay_s": 0,
    },
    # We will send over a lot of queries. This will make sure replicas are
    # killed quickly during cleanup.
    graceful_shutdown_timeout_s=1,
    max_concurrent_queries=1000,
    version="v1",
)
class Heavy:
    def __call__(self):
        time.sleep(5)

app = Heavy.bind()
