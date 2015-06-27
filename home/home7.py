def checkio(res):
    if res[0][0] == res[0][1] == res[0][2]:
        return res[0][1]
    if res[1][0] == res[1][1] == res[1][2]:
        return res[1][0]
    if res[2][0] == res[2][1] == res[2][2]:
        return res[2][0]

    if res[0][0] == res[1][0] == res[2][0]:
        return res[0][0]
    if res[0][1] == res[1][1] == res[2][1]:
        return res[1][1]
    if res[0][2] == res[1][2] == res[2][2]:
        return res[2][2]

    if res[0][0] == res[1][1] == res[2][2]:
        return res[0][0]
    if res[2][0] == res[1][1] == res[0][2]:
        return res[1][1]
    return 'D'

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio([
        u"X.O",
        u"XX.",
        u"XOO"]))
    print(checkio([
        u"OO.",
        u"XOX",
        u"XOX"]))
    print(checkio([
        u"OOX",
        u"XXO",
        u"OXX"]))
