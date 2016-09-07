from main_handler import *
from database import *


class PostView(Handler):
    def get(self, post_id):
        post_id = int(post_id)
        post = Posts.get_by_id(post_id)
        if post:
            self.render("post.html", title="Post", post=post)
        else:
            self.error(404)
            self.write("404 Page not found")