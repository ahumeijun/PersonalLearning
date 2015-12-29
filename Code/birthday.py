#! /usr/bin/env python
# -*- coding: utf-8 -*-

def samebirth(n):
    p = 1.0
    for i in range(0, n):
        p = p * (365 - i) / 365
    return 1 - p
    
if __name__ == '__main__':
    for n in range(1, 100, 1):
        print('%d个人中至少两个人同一天生日的概率: %.10f'%(n, samebirth(n)))