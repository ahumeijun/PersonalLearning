# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import time

def log(level):
    def decorator(func):
        def wrapper(*args, **kw):
            start = time.time()
            result = func(*args, **kw)
            interval = time.time() - start
            print('{level}: call function {name} spends {time} seconds.'.format(level=level, name=func.__name__, time=interval))
            return result
        return wrapper
    return decorator

@log('DEBUG')
def testCase1():
    print('hello, world!')

@log('INFO')
def testCase2(name):
    print('good morning, {name}!'.format(name=name))

@log('WARN')
def testCase3():
    return "FOOBAR"

def main():
    testCase1()
    testCase2('python')
    foobar = testCase3()
    print(foobar)

if __name__ == '__main__':
    main()