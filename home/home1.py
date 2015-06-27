# the best solution
# def checkio(string):
#     'return sentence without extra spaces'
#     return '-'.join(string.replace('-',' ').split()


def checkio(line):
    out = []
    for i in line.split('-'):
        if i:
            out.append(i)
            #replace this for solution
    return '-'.join(i for i in out)


if __name__ == '__main__':
    assert checkio('I--like---python') == "I-like-python"
    # print checkio('I--like---python')
