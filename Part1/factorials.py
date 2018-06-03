#!/usr/bin/env python

def factorial(n):
    result = 1;

    for i in range(1, n+1):
        result *= i

    return result

if __name__ == '__main__':
    n = int(input())
    print(factorial(n))
