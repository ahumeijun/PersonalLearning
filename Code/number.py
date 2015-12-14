#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isSxh(num):
    sum = 0
    for char in num:
        n = int(char)
        sum += n ** 3
    return sum == int(num)


def  isHws(num):
    length = len(num)
    for i in range(0, length / 2):
        if num[i] != num[length - 1 -i]:
            return False
    else:
        return True

num = raw_input(':>')
sxh = isSxh(num)
hws = isHws(num)

if sxh:
    print('ssss')

if hws:
    print('hhhh')

if not sxh and not hws:
    print('!!!!')

