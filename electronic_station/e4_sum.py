# -*- coding: utf-8 -*-

# Fucking awesome!
# checkio=eval("su"+"m")

s = 0


def checkio(data):
    global s
    if data:
        s += data.pop()
        return checkio(data)
    else:
        rt = s
        s = 0
        return rt


print(checkio([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(checkio([1, 2]))
