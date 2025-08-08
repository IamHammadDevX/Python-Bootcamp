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


decorated_function = delay_decorator(say_greet)
decorated_function()