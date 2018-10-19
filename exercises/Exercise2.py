import math


def distance(px1, py1, px2, py2):
    return math.sqrt((px2 - px1) ** 2 + (py2 - py1) ** 2)


x1 = int(input('Point 1 x-cord\n'))
y1 = int(input('Point 1 y-cord\n'))
x2 = int(input('Point 2 x-cord\n'))
y2 = int(input('Point 2 y-cord\n'))

print(distance(x1, y1, x2, y2))

