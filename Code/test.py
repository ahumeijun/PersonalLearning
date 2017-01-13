#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys 
sys.setrecursionlimit(1000000)

# def sum(n):
# 	if n == 0:
# 		return n
# 	else:
# 		return n + sum(n-1)


# def feb(n):
# 	if n == 0:
# 		return 1;
# 	elif n == 1:
# 		return 1;
# 	else:
# 		return feb(n - 1) + feb(n-2)

# def han(n, A, B, C):
# 	if n == 1:
# 		print (A + ' -> ' + C)
# 	else:
#         han(n - 1, A, C, B)
# 		print (A + ' -> ' + C)
# 		han(n - 1, B, A, C)

# print(sum(100))
# print(feb(10))


# han(5, 'A', 'B', 'C')

for i in range(1, 10):
    for j in range(1, 10):
        if i * j * (i * 10 + j) == j * 100 + j * 10 + j:
            print '*********'
            print("%s %s"%(i, j))
            print '*********'
print("end")