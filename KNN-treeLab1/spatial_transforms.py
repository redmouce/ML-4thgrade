import math


def normal(x, y):
    return (x, y)


def mult(x, y, n=2):
    return [x, y] * n


def angle(x, y, angle=30):
    return (math.cos(x), math.cos(y))
