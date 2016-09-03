from google.appengine.ext import db


def find_first(condition, data):
    user = Users.all().filter(condition, data).get()
    return user


def get_username_by_id(user_id):
    return Users.get_by_id(int(user_id)).name


class Users(db.Model):
    name = db.StringProperty(required=True)
    password_hash = db.StringProperty(required=True)
    email = db.EmailProperty(default=" ")
    created_date = db.DateTimeProperty(auto_now_add=True)
    rating = db.IntegerProperty()


class Posts(db.Model):
    user_id = db.IntegerProperty(required=True)
    title = db.StringProperty(required=True)
    post = db.TextProperty(required=True)
    created_date = db.DateTimeProperty(auto_now_add=True)
    last_modified_date = db.DateTimeProperty(auto_now=True)
