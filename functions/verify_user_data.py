import re
import database


class UserData(object):
    def __init__(self, name, password, password_verify, email=""):
        self.username = name
        self.password_verify = password_verify
        self.password = password
        self.email = email


class VerifyUserData(UserData):
    def __init__(self, name, password, password_verify, email=""):
        super(VerifyUserData, self).__init__(name, password, password_verify, email)
        self.invalid_name = ""
        self.already_exists = ""
        self.invalid_password = ""
        self.password_not_match = ""
        self.invalid_email = ""

    def valid_name(self):
        s_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return s_re.match(self.username)

    def valid_password(self):
        s_re = re.compile(r"^.{3,20}$")
        return s_re.match(self.password)

    def valid_email(self):
        s_re = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
        return s_re.match(self.email)

    def password_match(self):
        if self.password == self.password_verify:
            return True
        return False

    def make_check(self):
        if database.find_first("name =", self.username):
            self.already_exists = "User already exists"
        if not self.username:
            self.invalid_name = "Name is missing"
        elif not self.valid_name():
            self.invalid_name = 'Name is invalid'

        if not self.password:
            self.invalid_password = 'Password is missing'
        elif not self.valid_password():
            self.invalid_password = 'Password is invalid'
        elif self.password != self.password_verify:
            self.password_not_match = 'Password doesn\'t match'

        if self.email and not self.valid_email():
            self.invalid_email = 'Emails is invalid'

        if not (self.invalid_name or
                self.invalid_password or
                self.password_not_match or
                self.invalid_email or
                self.already_exists):
            return True
