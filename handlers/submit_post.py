from google.appengine.api import memcache

from main_handler import *
from database import *
from functions.cache import cache


class SubmitPost(Handler):
    def render_front(self, title="", content="", error=""):
        self.render("submit.html", title=title, content=content, error=error)

    def get(self, *args, **kwargs):
        self.render_front()

    def post(self, *args, **kwargs):
        title = self.request.get('subject')
        content = self.request.get('content')

        if title and content:
            post = Posts(title=title, content=content)
            post.put()
            post_id = post.key().id()
            cache(str(post_id), post, update=True)
            memcache.delete('posts_top_10')

            return self.redirect("/blog/%s" % post_id)
        else:
            error = "We need both title and artwork!"
            self.render_front(title=title, content=content, error=error)
