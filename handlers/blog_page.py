from main_handler import *


class BlogPage(Handler):
    def get(self, *args):
        self.render('index.html')
