# -*- coding: utf-8 -*-
# py3

import string


def role(s1, s2):
    return sum([int(s1[-1] == s2[-1]) * 10 + int(s1[0] == s2[0]) * 10,
                min(len(s1), len(s2)) / max(len(s1), len(s2)) * 30,
                len(set(s1) & set(s2)) / len(set(s1) | set(s2)) * 50])


def find_word(message):
    row = (message.translate(
        message.maketrans(string.punctuation,
                          len(string.punctuation) * " ")).lower()).split()
    matrix = {}
    ans = 0
    for x, r in enumerate(row):
        total = 0
        for y, c in enumerate(row):
            if x != y:
                total += role(r, c)
        ans = max(ans, total / (len(row) - 1))
        matrix[total / (len(row) - 1)] = r

    return matrix[ans]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word(
        "The Doors of Durin, Lord of Moria. Speak friend and enter. "
        "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(
        "One, two, two, three, three, three.") == "three", "Repeating"
