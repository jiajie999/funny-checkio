# encoding: utf-8
__author__ = 'mars'

#def checkio(text):
#    return max(string.ascii_lowercase, key=lambda ch: text.lower().count(ch))
""" 上面max的第一个参数是个iterable，第二个参数是一个函数，相当于对每个item应用后面的函数得到一个列表后取最大的 """


def checkio(text):
    a = sorted(filter(lambda x: x.isalpha(), text.lower()))
    b = {}
    [b.setdefault(a.count(i), i) for i in a]
    return b[max(b.keys())]
    #return max(b)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
