from main_handler import *
import database
from functions import hashing
from functions import check


class LoginPage(Handler):
    def get(self, *args, **kwargs):
        self.render("login.html")

    def post(self, *args, **kwargs):
        username = self.request.get("username")
        password = self.request.get("password")

        if check.user_exist(username, password):
            user_id = database.find_first("name =", username).key().id()
            cookie = hashing.make_hash(str(user_id), return_value=user_id, secret=True)
            self.response.set_cookie("user_id", cookie)
            self.redirect("/blog/welcome")
        else:
            self.render("login.html", username=username, error="Invalid login or password")
