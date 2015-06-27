__author__ = 'mars'


def checkio(data):
    data.sort()
    if len(data) % 2 == 0:
        return (float(data[len(data) / 2]) + float(data[len(data) / 2 - 1])) / 2
    else:
        return data[len(data) / 2]


print(checkio([3, 1, 2, 5, 3]))
