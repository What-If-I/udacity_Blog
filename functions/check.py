import database
import hashing


def user_exist(username, password):
    user = database.find_first("name =", username)
    if user and hashing.valid_hash([username, password], user.password_hash):
        return True
