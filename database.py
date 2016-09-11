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
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    def as_dict(self):
        dictionary = {"content": self.content,
                      "subject": self.title,
                      "created": self.created.strftime("%d-%m-%Y")
                      }
        return dictionary
