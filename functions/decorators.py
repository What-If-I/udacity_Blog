from handlers.main_handler import *


class MyDecorator(webapp2.RedirectHandler):

    def __init__(self, f):
        super(MyDecorator, self).__init__()
        self.initialize(request, response)
        print "inside myDecorator.__init__()"
        self.f = f  # Prove that function definition has completed

    def __call__(self, *args, **kwargs):
        print "Entering", self.f.__name__
        print "Exited", self.f.__name__
        self.response.out.write("Hello")
        return self.f(self, *args, **kwargs)


def require_login(func):
    def inner(*args, **kwargs):
        print "Hello"
        webapp2.RedirectHandler.request.cookies.get('user_id')
        webapp2.RedirectHandler.response.out.write("Hello")
        return func(*args, **kwargs)

    return inner


@MyDecorator
def print_x(x):
    print x
    return None
