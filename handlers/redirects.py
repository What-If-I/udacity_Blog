from main_handler import *


class RedirectToBlog(Handler):
    def get(self, *args):
        return self.redirect('/blog')
