def checkio_best(number):
    'return roman numeral using the specified integer value from range 1...3999'
    roman = ''
    romanmappings = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
                     40: "XL", 50: "L", 90: "XC", 100: "C",
                     400: "CD", 500: "D", 900: "CM", 1000: "M"}
    for intVal in sorted(romanmappings.keys(), reverse=True):
        while number >= intVal:
            roman += romanmappings[intVal]
            number -= intVal
    return roman


def checkio(data):
    roman = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
             40: "XL", 50: "L", 90: "XC", 100: "C",
             400: "CD", 500: "D", 900: "CM", 1000: "M"}
    n = 0
    res = ''
    while data > 0:
        for num in sorted(roman.keys(), reverse=True):
            if data >= num:
                res += (data / num) * roman[num]
                n = num
                break
        data -= (data / n) * n
    return res


if __name__ == '__main__':
    print(checkio(98))
    #MMMCMXCIX
    #assert checkio(6) == 'VI', '6'
    #assert checkio(76) == 'LXXVI', '76'
    #assert checkio(499) == 'CDXCIX', '499'

