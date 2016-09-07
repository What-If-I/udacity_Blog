from main_handler import *
from database import *


class BlogPage(Handler):
    def get(self, *args):
        posts = Posts.all().order('-created').fetch(limit=10)
        self.render('index.html', posts=posts)
