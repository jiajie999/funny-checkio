#!/usr/bin/env python
# -*- coding: utf-8 -*-


# best answer
# checkio=lambda d:[x for x in d if d.count(x)>1]

def checkio(data):
    l = list(data)
    o = []
    for i in l:
        if 1 < l.count(i):
            o.append(i)
    return o

# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# or remove elements from original list (but it's bad practice for many real cases)
# Loop over original list


if __name__ == "__main__":
    # print checkio([1, 2, 3, 1, 3])
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"