# -*- coding: utf-8 -*-
def checkio(expr):
    mapbract = {'}': '{', ')': '(', ']': '['}
    stack = []
    for i in expr:
        if i in mapbract.values():
            stack.append(i)
        elif i in mapbract.keys():
            if len(stack) > 0 and stack[-1] == mapbract[i]:
                stack.pop()
            else:
                return False
    if len(stack) > 0:
        return False
    else:
        return True


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"((5+3)*2+1)") == True, "Simple"
    assert checkio(u"{[(3+1)+2]+}") == True, "Different types"
    assert checkio(u"(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio(u"[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio(u"(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
