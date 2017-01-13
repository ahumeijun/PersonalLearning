# -*- coding: utf-8 -*-
#!/usr/bin/env python

import math

def A(m ,n):
    ret = math.factorial(n) / math.factorial(n-m)
    return ret

def C(m, n):
    ret = A(m, n) / math.factorial(m)
    return ret

def cell(i, n, count):
    ret = (-1 ** i) * C(i, count) * ((1 - float(i) / count) ** n)
    print ret
    return ret

def getAllCards(n, count):
    cells = 0;
    for i in range(1, count):
        cells += cell(i, n, count)
    return 1 + cells

if __name__ == '__main__':
    print "***************\n"+ str(getAllCards(108, 108))