# -*- coding: utf-8 -*-
import collections


def check_d(matrix, x, y):
    d = []
    for i in range(4):
        if x + i < len(matrix) and i + y < len(matrix):
            d.append(matrix[x + i][y + i])

    if check_t(d):
        return True

    d = []
    for i in range(4):
        if 0 <= x - i < len(matrix) and i + y < len(matrix):
            d.append(matrix[x - i][y + i])

    if check_t(d):
        return True
    return False


def m(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if check_d(matrix, i, j):
                return True
    return False


def check_v(matrix):
    length = len(matrix)
    for x in range(length):
        v = []
        for y in range(length):
            v.append(matrix[y][x])
        if check_t(v):
            return True
    return False


def check_h(matrix):
    for i in matrix:
        print(i)
        if check_t(i):
            return True

    return False


def check_t(t):
    for i in range(len(t)):
        tt = t[i:i + 4]
        print(tt)
        rt = collections.Counter(tt)
        if len(rt) == 1 and rt.values()[0] == 4:
            return True
    return False


def checkio(matrix):
    d = m(matrix)
    h = check_h(matrix)
    v = check_v(matrix)
    print(d, v, h)
    if d or h or v:
        return True
    return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    # assert checkio([
    #     [7, 1, 4, 1],
    #     [1, 2, 5, 2],
    #     [3, 4, 1, 3],
    #     [1, 1, 8, 1]
    # ]) == False, "Nothing here"
    # assert checkio([
    #     [2, 1, 1, 6, 1],
    #     [1, 3, 2, 1, 1],
    #     [4, 1, 1, 3, 1],
    #     [5, 5, 5, 5, 5],
    #     [1, 1, 3, 1, 1]
    # ]) == True, "Long Horizontal"
    # assert checkio([
    #     [7, 1, 1, 8, 1, 1],
    #     [1, 1, 7, 3, 1, 5],
    #     [2, 3, 1, 2, 5, 1],
    #     [1, 1, 1, 5, 1, 4],
    #     [4, 6, 5, 1, 3, 1],
    #     [1, 1, 9, 1, 2, 1]
    # ]) == True, "Diagonal"
    assert checkio(
        [[1, 9, 7, 8, 9, 3, 6, 5, 6, 2], [4, 9, 4, 8, 3, 4, 8, 8, 5, 9],
         [2, 8, 5, 5, 7, 8, 6, 1, 3, 6], [6, 4, 7, 6, 9, 1, 4, 5, 7, 8],
         [4, 7, 7, 9, 8, 8, 8, 8, 4, 4], [3, 7, 3, 2, 1, 9, 1, 8, 9, 1],
         [4, 7, 2, 4, 8, 1, 2, 3, 6, 2], [4, 4, 1, 3, 3, 3, 9, 2, 6, 7],
         [8, 6, 1, 9, 3, 5, 8, 1, 7, 5],
         [7, 3, 6, 5, 3, 6, 6, 4, 8, 2]]) == True
