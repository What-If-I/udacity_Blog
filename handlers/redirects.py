from main_handler import *


class RedirectToMainPage(Handler):
    def get(self, *args):
        return self.redirect('/blog')
