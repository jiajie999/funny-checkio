# -*- coding: utf-8 -*-


def checkio(text):
    rt = filter(lambda x: not x.isalpha(), text)
    rt = filter(lambda x: len(x.split('.')) == 4, rt.split())
    count = 0
    s = []
    for i in rt:
        for j in i.split('.'):
            if j.isalnum() and len(j) <= 3:
                if 255 >= int(j) >= 0:
                    count += 1
        if count == len(i.split('.')):
            s.append(i)
        count = 0
    return s


if __name__ == '__main__':
    # print checkio("00250.00001.0000002.1 251.1.2.1")
    assert checkio("192.168.1.1 and 10.0.0.1 or 127.0.0.1") == \
           ["192.168.1.1", "10.0.0.1", "127.0.0.1"], "All correct"
    #assert checkio("10.0.0.1.1 but 127.0.0.256 1.1.1.1") == \
    #       ["1.1.1.1"], "Only 1.1.1.1"
    assert checkio("167.11.0.0 1.2.3.255 192,168,1,1") == \
           ["167.11.0.0", "1.2.3.255"], "0 and 255"
    assert checkio("267.11.0.0 1.2.3.4/16 192:168:1:1") == \
           [], "I don't see IP"
    assert checkio("00250.00001.0000002.1 251.1.2.1") == \
           ["251.1.2.1"], "Be careful with zeros"