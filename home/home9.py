# -*- coding: utf-8 -*-
def checkio(data):
    a = data.split(':')
    rt = "%s : %s : %s" % (co1(a[0]), co23(a[1]), co23(a[2]))
    rt = rt.replace('0', '.').replace('1', '-')
    return rt


def co1(num):
    if len(num) == 1:
        return "{0:02b}".format(int(0)) + ' ' + "{0:04b}".format(int(num))
    else:
        return "{0:02b}".format(int(num[0])) + ' ' + "{0:04b}".format(int(num[1]))


def co23(num):
    if len(num) == 2:
        return "{0:03b}".format(int(num[0])) + ' ' + "{0:04b}".format(int(num[1]))
    else:
        return "{0:03b}".format(0) + ' ' + "{0:04b}".format(int(num))


def checkio_best(data):
    ret = []
    for i, d in enumerate(data.split(':')):
        r, d = '', int(d)
        f, s = d / 10, d % 10
        if i == 0:
            r += '{0:02b} '.format(f)
        else:
            r += '{0:03b} '.format(f)
        r += '{0:04b}'.format(s)
        ret.append(r)
    ret = ' : '.join(ret)
    return ret.replace('0', '.').replace('1', '-')


if __name__ == '__main__':
    print(checkio("7:41:37"))
    print(".. .--- : -.. ...- : .-- .---")
