# def add(*args):
#     den = 0
#     for n in args:
#         den += n
#     print(den)
#
#
# add(4, 6, 7, 1, 2, 5)

def calculate(n, **kwargs):
    print(kwargs['add'])
    n += kwargs["add"]
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan")
print(my_car.model)

def test(*args):
    print(args)

test(1,2,3,4,5)