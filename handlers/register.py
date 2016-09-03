from functions import hashing
from functions.verify_user_data import *
from main_handler import *


class RegisterPage(Handler):
    def get(self, *args):
        self.render('register.html', error="")

    def post(self, *args):
        username = self.request.get("username")
        password = self.request.get("password")
        password_verify = self.request.get("verify")
        email = self.request.get("email")

        user = UserData(username, password, password_verify, email)
        verified = VerifyUserData(user.username, user.password, user.password_verify, user.email)

        if not email:
            email = "No"

        if not verified.make_check():
            self.render("register.html", username=user.username, email=user.email, error=verified)
        else:
            pw_hash = hashing.make_hash([username, password])
            db_user = database.Users(name=username, password_hash=pw_hash, email=email)
            db_user.put()

            user_id = str(db_user.key().id())
            cookie = hashing.make_hash(user_id, return_value=user_id, secret=True)

            self.response.set_cookie("user_id", cookie)
            self.redirect('/blog/welcome')
