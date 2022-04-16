import math


def triangle_perimeter(a=7, b=2, c=8):
    res = int(a) + int(b) + int(c)
    print(res)


def triangle_area(a=7, b=2, c=8):
    pp = (int(a) + int(b) + int(c)) * 0.5  # полупериметр
    pp_multi = pp * (pp - a) * (pp - b) * (pp - c)
    res = math.sqrt(pp_multi)

    print(res)
