# -*- coding: utf-8 -*-


def is_bigger_9(s):
    if ord(s) >= 65:
        return True
    else:
        return False


def chr2num(c):
    for i in c:
        if is_bigger_9(i):
            return ord(i) - 55
        else:
            return int(i)


def k2ten(k, x):
    ans = 0
    for index, num in enumerate(x):
        ans += chr2num(num) * pow(k, (len(x) - index - 1))
    return ans


def bigger_item(num, k):
    for i in num:
        if k <= chr2num(i):
            return False
    return True


def checkio(number):
    """
    Find min K
    """
    ans = 0

    for k in xrange(2, 37):

        x = k2ten(k, number)

        s, r = divmod(x, k - 1)
        if r == 0 and bigger_item(number, k):
            print(s, r, k, number)
            ans = k
            # break
    return ans


def best_checkio(number):
    """
    This answer is useful,because of int() could have base parameter!
       And!!! catch ValueError done the work that my bigger_item done!

    @param number:
    @return:
    """
    for base in range(2, 37):
        try:
            if not int(number, base) % (base - 1):
                return base
        except ValueError:
            pass
    return 0


def shortest_checkio(number):
    """
    Given a number in an unknown radix, return radix k such that (k-1) | number.
    Return 0 if such a radix does not exist.
    """
    return next((k for k in range(max(2, 1 + int(max(number), 36)), 37) if
                 not int(number, k) % (k - 1)), 0)


if __name__ == '__main__':
    print(int(u"1010101011", 2))
    print(checkio(u"18"))
    # print k2ten(10,'18')
    # print k2ten(2,"1010101011")
    # print checkio(u"1010101011")
    # print checkio(u"222")
    # print checkio(u"A23B")
    # assert checkio(u"18") == 10, "Simple decimal"
    # assert checkio(u"1010101011") == 2, "Any number is divisible by 1"
    # assert Best_checkio(u"222") == 3, "3rd test"
    # assert Best_checkio(u"A23B") == 14, "It's not a hex"
    # print('Local tests done')
