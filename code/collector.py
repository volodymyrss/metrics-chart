import time
import requests
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server


class CustomCollector(object):
    def __init__(self):
        pass

    def collect(self):
        N = requests.get("https://crux-private.obsuks1.unige.ch/tasks/summary").json()['tasks']['waiting']

        g = GaugeMetricFamily("QueueSize", 'Help text', labels=['app'])
        g.add_metric(["dqueue.waiting"], N)
        yield g

#        c = CounterMetricFamily("HttpRequests", 'Help text', labels=['app'])
#        c.add_metric(["example"], 2000)
#        yield c


if __name__ == '__main__':
    start_http_server(8000)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(1)
