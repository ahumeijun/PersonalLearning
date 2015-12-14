#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random

def recursion_change(money):
    divisor = 1;
    if money >= 100:
        divisor = 100
    elif money >= 50:
        divisor = 50
    elif money >= 20:
        divisor = 20
    elif money >= 10:
        divisor = 10
    elif money >= 5:
        divisor = 5
    quotient = money / divisor
    remainder = money % divisor
    result = '￥%dx%d'%(divisor, quotient)
    if remainder > 0:
        return result + ' & ' + recursion_change(remainder)
    else:
        return result

def loop_change(money):
    result = ''
    remainder = money
    while remainder != 0:
        divisor = 1;
        if remainder >= 100:
            divisor = 100
        elif remainder >= 50:
            divisor = 50
        elif remainder >= 20:
            divisor = 20
        elif remainder >= 10:
            divisor = 10
        elif remainder >= 5:
            divisor = 5
        quotient = remainder / divisor
        remainder = remainder % divisor
        temp = '￥%dx%d'%(divisor, quotient)
        if len(result) != 0:
            result += ' & '
        result += temp
    return result


if __name__ == '__main__':
    for i in range(1, 20):
        money = random.randint(1, 1000)
        print(money)
        print('recursion: %s'%recursion_change(money))
        print('loop     : %s'%loop_change(money))

