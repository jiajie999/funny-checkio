__author__ = 'mars'

"""
Stephen's speech module is broken. This module is responsible for his number pronunciation.
He has to click to input all of the numerical digits in a figure,
so when there are big numbers it can take him a long time.
Help the robot to speak properly and increase his number processing speed by writing a new speech module for him.
All the words in the string must be separated by exactly one space character.

Input: An integer from 0 to 999.
Output: A string representation of this number.
How it is used: It can be useful for the speech synthesis software or automatic reports systems.
"""

FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    if number >= 100:
        if number % 10 != 0:
            return FIRST_TEN[number / 100] + ' ' + HUNDRED + ' ' + checkio(number % 100)
        else:
            rt = FIRST_TEN[number / 100] + ' ' + HUNDRED + ' ' + checkio(number % 100)
            if rt.find('zero') != -1:
                rt = " ".join(rt.split()[:-1])
            return rt

    if 19 < number <= 99:
        d = {}
        [d.setdefault(i, OTHER_TENS[i / 10 - 2]) for i in range(20, 100, 10)]
        rt = d.get(number / 10 * 10) + ' ' + checkio(number % 10)
        if rt.find('zero') != -1:
            rt = " ".join(rt.split()[:-1])
        return rt

    if 9 < number <= 19:
        d = {}
        [d.setdefault(i, SECOND_TEN[i - 10]) for i in range(10, 20)]
        rt = d.get(number)
        return rt

    if number <= 9:
        rt = FIRST_TEN[number]
        return rt


if __name__ == '__main__':
    print(checkio(20))
    #assert checkio(4) == 'four', "1st example"
    #assert checkio(12) == 'twelve', "3rd example"
    #assert checkio(40) == 'forty', "6th example"
    #assert checkio(51) == 'fifty one', "6th example"
    #assert checkio(101) == 'one hundred one', "4th example"
    #assert checkio(212) == 'two hundred twelve', "5th example"
    #assert checkio(133) == 'one hundred thirty three', "2nd example"