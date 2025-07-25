def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum, args, type(args))

add(1,2,3,4,5)

def calcualtion(**kwargs):
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        print(value)

calcualtion(add = 2, sub = 34)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(model="GT-R")
print(my_car.make)