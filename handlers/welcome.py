from main_handler import *
from functions import hashing
import database


class WelcomePage(Handler):
    def get(self, *args, **kwargs):
        user_id_cookie = self.request.cookies.get('user_id')

        if user_id_cookie and hashing.valid_user_cookie(user_id_cookie):
            user_name = database.get_username_by_id(user_id_cookie.split("|")[0])
            self.write("Hello %s!" % user_name)
        else:
            self.redirect("/blog/signup/")