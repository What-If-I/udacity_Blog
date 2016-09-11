import time
from google.appengine.api import memcache
from main_handler import *
from database import *
from functions.cache import cache


class PostView(Handler):
    def get(self, post_id):

        post_id = int(post_id)
        post = cache(str(post_id), Posts.get_by_id(post_id))

        if post:
            self.render("post.html", title="Post", post=post.data, last_cached_time=int(time.time() - post.timestamp))
        else:
            self.error(404)
            self.write("404 Page not found")