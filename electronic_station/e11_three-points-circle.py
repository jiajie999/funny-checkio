# -*- coding: utf-8 -*-

from decimal import Decimal
from math import sqrt, hypot


def checkio(data):
    a, b, c = data.split("),(")
    x1, y1 = map(float, a.replace('(', '').split(','))
    x2, y2 = map(float, b.replace('(', '').split(','))
    x3, y3 = map(float, c.replace(')', '').split(','))
    # Could use eval(data) to get input

    a = 2 * (x2 - x1)
    b = 2 * (y2 - y1)
    c = x2 * x2 + y2 * y2 - x1 * x1 - y1 * y1
    d = 2 * (x3 - x2)
    e = 2 * (y3 - y2)
    f = x3 * x3 + y3 * y3 - x2 * x2 - y2 * y2
    x = ((b * f - e * c) / (b * d - e * a))
    y = ((d * c - a * f) / (b * d - e * a))
    r = sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1))
    x, y, r = map(lambda f_num: '%g' % (Decimal(str(f_num))),
                  map(lambda s: "{s:0.2f}".format(s=s), [x, y, r]))
    return "(x-{x})^2+(y-{y})^2={r}^2".format(r=r, x=x, y=y)


from math import hypot
"""
hypot(x, y)

Return the Euclidean distance, sqrt(x*x + y*y).
"""

def checkio_best(data):
    (x1, y1), (x2, y2), (x3, y3) = eval('[' + data + ']')
    d = lambda x, y: x * x + y * y
    t21 = [2 * (x2 - x1), 2 * (y2 - y1), d(x2, y2) - d(x1, y1)]
    t31 = [2 * (x3 - x1), 2 * (y3 - y1), d(x3, y3) - d(x1, y1)]

    det = lambda i, j: t21[i] * t31[j] - t21[j] * t31[i]
    a = det(2, 1) / det(0, 1)
    b = det(0, 2) / det(0, 1)
    r = hypot(x1 - a, y1 - b)

    return '(x-{:.3g})^2+(y-{:.3g})^2={:.3g}^2'.format(a, b, round(r, 2))


if __name__ == '__main__':
    print(checkio("(2,2),(1,4),(2,5)"))
    print(checkio("(2,2),(6,2),(2,6)"))
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
