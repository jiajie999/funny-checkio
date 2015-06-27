# -*- coding: utf-8 -*-


def letter_queue(commands):
    tmp = []
    for cmd in commands:
        c = cmd.split(' ')
        if len(c) > 1:
            d = c[1]
        c = c[0]
        if c == 'PUSH':
            tmp.append(d)
        else:
            if tmp:
                tmp.pop(0)

    return "".join(tmp)


if __name__ == "__main__":
    pass