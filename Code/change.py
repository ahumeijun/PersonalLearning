#! /usr/bin/env python
# -*- coding: utf-8 -*-

def for_change(change):
    while change > 100:
        change -= 100
    change_1 = ''
    if change >= 50:
        change_1 = change_1 + ', 50'
        change -= 50
    elif change >= 20:
        change_1 = change_1 + ', 20'
        change -= 20
    elif change >= 10:
        change_1 = change_1 + ', 10'
        change -= 10
    elif change >= 5:
        change_1 = change_1 + ', 5'
        change -= 5
    elif change >= 1:
        change_1 = change_1 + ', 1'
        change -= 1
    if change > 0:
        return change_1 + for_change(change)
    else:
        return change_1
        
        
def ret():
    return "aaaaa"

def test(a):
    ret()
    print(a)

if __name__ == '__main__':
    