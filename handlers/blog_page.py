import time

from main_handler import *
from database import *
from functions.cache import cache


class BlogPage(Handler):
    def get(self, *args):
        cached = cache('posts_top_10', Posts.all().order('-created').fetch(limit=10))
        self.render('index.html', posts=cached.data, last_cached_time=int(time.time() - cached.timestamp))
