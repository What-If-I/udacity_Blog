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


# def get(self, post_id):
#     post_id = int(post_id)
#     post = Posts.get_by_id(post_id)
#     post_dict = {"content": post.content,
#                  "title": post.title,
#                  "created": post.created.strftime("%d-%m-%Y")
#                  }
#     json_output = json.dumps(post_dict)
#     if post:
#         self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
#         self.write(json_output)
#     else:
#         self.error(404)
#         self.write("404 Page not found")