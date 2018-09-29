import random
import math


def findPI(n):
    m = 0
    for i in range(n):
        y = random.random()
        alpha = random.random() * math.pi
        if (y + 0.5 * math.sin(alpha)) > 1 or (y - 0.5 * math.sin(alpha)) < 0:
           m += 1
    try:
        return 2*n / m;
    except ZeroDivisionError:
        print("Недостаточно успешных попыток")
