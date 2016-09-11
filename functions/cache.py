import time
from collections import namedtuple
from google.appengine.api import memcache

Cache = namedtuple("Cache", "data timestamp")


def cache(key, queue, update=False):
    cached = memcache.get(key)
    if cached and not update:
        return cached
    else:
        print 'Updated!'
        cached = Cache(queue, time.time())
        memcache.set(key, cached)
    return cached
