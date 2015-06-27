# -*- coding: utf-8 -*-
def weak_point(matrix):
    """From this task, you can learn how to use min(*args,key=fun)
    :param matrix:
    :return:
    """
    v = {}
    h = {}
    for i in xrange(len(matrix)):
        v[i] = sum(matrix[i])
        h[i] = sum(matrix[j][i] for j in xrange(len(matrix)))
    return min(v.keys(), key=lambda x: v[x]), min(h.keys(), key=lambda x: h[x])


if __name__ == '__main__':
    print(list(weak_point([[7, 2, 7, 2, 8],
                           [2, 9, 4, 1, 7],
                           [3, 8, 6, 2, 4],
                           [2, 5, 2, 9, 1],
                           [6, 6, 5, 4, 5]])))
    assert isinstance(weak_point([[1]]),
                      (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
