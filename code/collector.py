import time
import requests
from prometheus_client.core import REGISTRY, Metric
#from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server


class CustomCollector(object):
    def __init__(self):
        pass

    def collect(self):
        n = "oda_dqueue"
        m = Metric(n, 'Help text', 'gauge')

        #g = GaugeMetricFamily()
        for c in ["public", "private"]:
            d = requests.get("https://crux-" + c + ".obsuks1.unige.ch/tasks/summary").json()['tasks']

            for k, v in d.items():
                m.add_sample(n, value=v, labels={'oda-dda-class': c, 'state': k})

        yield m

#        c = CounterMetricFamily("HttpRequests", 'Help text', labels=['app'])
#        c.add_metric(["example"], 2000)
#        yield c


if __name__ == '__main__':
    start_http_server(8000)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(1)
