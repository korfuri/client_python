#!/usr/bin/python

from . import core
from . import exposition
from . import process_collector

__all__ = ['Counter', 'Gauge', 'Summary', 'Histogram']
# http://stackoverflow.com/questions/19913653/no-unicode-in-all-for-a-packages-init
__all__ = [n.encode('ascii') for n in __all__]

CollectorRegistry = core.CollectorRegistry
REGISTRY = core.REGISTRY
Metric = core.Metric
Counter = core.Counter
Gauge = core.Gauge
Summary = core.Summary
Histogram = core.Histogram

CONTENT_TYPE_LATEST = exposition.CONTENT_TYPE_LATEST
generate_latest = exposition.generate_latest
MetricsHandler = exposition.MetricsHandler
start_http_server = exposition.start_http_server
write_to_textfile = exposition.write_to_textfile

ProcessCollector = process_collector.ProcessCollector
PROCESS_COLLECTOR = process_collector.PROCESS_COLLECTOR


if __name__ == '__main__':
    c = Counter('cc', 'A counter')
    c.inc()

    g = Gauge('gg', 'A gauge')
    g.set(17)

    s = Summary('ss', 'A summary', ['a', 'b'])
    s.labels('c', 'd').observe(17)

    h = Histogram('hh', 'A histogram')
    h.observe(.6)

    start_http_server(8000)
    import time
    while True:
      time.sleep(1)
