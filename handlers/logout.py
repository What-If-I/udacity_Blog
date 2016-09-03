from main_handler import *


class LogoutPage(Handler):
    def get(self, *args, **kwargs):
        self.response.delete_cookie("user_id")
        self.redirect("/blog/signup")
