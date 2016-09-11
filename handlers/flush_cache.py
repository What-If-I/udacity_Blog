from google.appengine.api import memcache
from main_handler import *


class FlushCache(Handler):
    def get(self, *args, **kwargs):
        memcache.flush_all()
        self.redirect('/blog/')
