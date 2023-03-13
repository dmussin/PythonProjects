# from flask import Flask
# app = Flask(__name__)
#
# print(__name__)
# @app.route('/')
# def hello_world():
#     return '<h1 style="text-align: center">Hello, World!</h1>' \
#            '<p>This is a paragraph</p>' \
#            '<img src = "https://thumbs.gfycat.com/AmazingDazzlingFrog.webp" width=200>'
#
#
# def make_bold(func):
#     def wrap():
#         return '<b>' + func() + '</b>'
#     return wrap
#
# def make_emphasis(func):
#     def wrap():
#         return '<em>' + func() + '</em>'
#     return wrap
#
#
# def make_underlined(func):
#     def wrap():
#         return '<u>' + func() + '</u>'
#     return wrap
#
#
#
# @app.route('/bye')
# @make_bold
# @make_underlined
# @make_emphasis
#
# def say_bye():
#     return "Bye"
#
#
# @app.route('/username/<name>')
# def greet(name):
#     return f"Hello there!, {name}"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
# greet()


## Advanced Python Decorator Functions

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
# def is_auth_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
#
#
#
# @is_auth_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post")
#
# new_user = User("Dani")
# new_user.is_logged_in = True
# create_blog_post(new_user)


# ------------------------------

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper

@logging_decorator
def a_function(a, b, c):
    return a * b * c

a_function(1,2,3)

