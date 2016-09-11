import time
from collections import namedtuple
from google.appengine.api import memcache

Cache = namedtuple("Cache", "data timestamp")


def cache(key, queue, update=False):
    cached = memcache.get(key)
    if cached is not None and not update:
        return cached
    else:
        cached = Cache(queue, time.time())
        memcache.add(key, cached)
    return cached
