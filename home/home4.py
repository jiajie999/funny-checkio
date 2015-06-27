__author__ = 'mars'

#def checkio(data):
#    'Return True if password strong and False if not'
#    return bool(len(data) >= 10 \
#        and filter(lambda a:a.isupper(),data) \
#        and filter(lambda a:a.islower(),data) \
#        and filter(lambda a:a.isdigit(),data))

def checkio(data):
    if len(data) < 10:
        return False
    a, b, c = False, False, False
    for i in data:
        if i.isdigit():
            a = True
        elif i.islower():
            b = True
        elif i.isupper():
            c = True
    if a and b and c:
        return True
    else:
        return False


if __name__ == '__main__':
    #checkio("")
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
    print(filter(lambda a: a.isupper(), u'QwErTy911poqqqq'))
