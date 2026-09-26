import math


def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take sqrt of a negative number")
    return math.sqrt(x)