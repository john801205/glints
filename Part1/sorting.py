#!/usr/bin/env python

import copy
import sys

def isSorted(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i-1]:
            return False

    return True

def swap(numbers):
    numbers = copy.copy(numbers)
    index1 = 0

    while index1+1 < len(numbers) and numbers[index1] <= numbers[index1+1]:
        index1 += 1

    index2 = index1+1
    while index2+1 < len(numbers) and numbers[index2] == numbers[index2+1]:
        index2 += 1

    if not isSorted(numbers[index2:]):
        while index2+1 < len(numbers) and numbers[index2] <= numbers[index2+1]:
            index2 += 1

        if index2+1 < len(numbers) and numbers[index2] > numbers[index2+1]:
            index2 += 1

    numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

    if isSorted(numbers):
        return (index1, index2)
    else:
        return None

def reverse(numbers):
    numbers = copy.copy(numbers)
    index1 = 0

    while index1+1 < len(numbers) and numbers[index1] <= numbers[index1+1]:
        index1 += 1

    index2 = index1+1
    while index2+1 < len(numbers) and numbers[index2] >= numbers[index2+1]:
        index2 += 1

    i, j = index1, index2
    while i < j:
        numbers[i], numbers[j] = numbers[j], numbers[i]
        i += 1
        j -= 1

    if isSorted(numbers):
        return (index1, index2)
    else:
        return None


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))

    if isSorted(numbers):
        print('yes')
        sys.exit(0)

    s = swap(numbers)
    if s != None:
        print('yes')
        print('swap {0} {1}'.format(s[0]+1, s[1]+1))
        sys.exit(0)

    s = reverse(numbers)
    if s != None:
        print('yes')
        print('reverse {0} {1}'.format(s[0]+1, s[1]+1))
        sys.exit(0)

    print('no')


