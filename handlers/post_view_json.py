from main_handler import *
from database import *
from datetime import date
import json


class PostViewJson(Handler):
    def get(self, post_id):
        post_id = int(post_id)
        post = Posts.get_by_id(post_id)
        json_output = json.dumps(post.as_dict())
        if post:
            self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
            self.write(json_output)
        else:
            self.error(404)
            self.write("404 Page not found")
