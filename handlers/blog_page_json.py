from main_handler import *
from database import *
import json


class BlogPageJson(Handler):
    def get(self, *args):
        posts = Posts.all().order('-created').fetch(limit=10)
        posts_list = list()
        for post in posts:
            post_dict = {"content": post.content,
                         "subject": post.title,
                         "created": post.created.strftime("%d-%m-%Y")
                         }
            posts_list.append(post_dict)
        json_output = json.dumps(posts_list)
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        self.write(json_output)