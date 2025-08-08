import time

def delay_decorator(function):
    def wrapper_func():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something After

    return wrapper_func

@delay_decorator
def say_hello():
    print("Hello World")


@delay_decorator
def greeting():
    print("How are you?")

def say_greet():
    print("What about you?")


# decorated_function = delay_decorator(say_greet)
# decorated_function()

class USER:
    def __init__(self, name):
        self.name = name
        self.is_login = False

def is_auth_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_login == True:
            function(args[0])
    return wrapper


@is_auth_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")


new_user = USER("Hanrie")
new_user.is_login = True
create_blog_post(new_user)


def order_food(*args):
    for item in args:
        print(f"You ordered: {item}")

order_food("Burger", "Fries", "Coke")


def make_smoothie(**kwargs):
    for fruit, quantity in kwargs.items():
        print(f"{quantity}x {fruit}")

make_smoothie(banana=2, mango=1, strawberry=3)
