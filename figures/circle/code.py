import math


def circle_area(r=5):
    res = math.pi * (int(r)**2)
    print(round(res, 1))


def circle_perimeter(r=5):

    print(2 * math.pi * r)
