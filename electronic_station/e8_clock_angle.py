# -*- coding: utf-8 -*-

# Not allowed on checkio, change to py3
# from __future__ import division


def clock_angle(time):
    h, m = map(int, time.split(":"))
    angle = abs(h % 12 * 30 + m / 2 - m * 6)
    return min(360 - angle, angle)


if __name__ == '__main__':

    assert clock_angle("12:01") == 5.5, "12:01"
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
