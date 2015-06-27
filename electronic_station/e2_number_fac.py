# -*- coding: utf-8 -*-
import itertools


def checkio(data):
    limit = len(str(data))
    rt = 0
    while rt == 0 and limit <= len(str(data)) + 2:
        for i in itertools.combinations_with_replacement([i for i in range(10)], limit):
            x = 1
            for j in i:
                x *= j
            if x == data:
                return int(''.join([str(j) for j in i]))
        limit += 1

    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(5) == 5, "5th example"
