#!/usr/bin/env python

import collections

if __name__ == '__main__':
    M, N, R = list(map(int, input().strip().split()))
    matrix = []

    for i in range(M):
        matrix.append(list(map(int, input().strip().split())))

    row, col = M, N
    i, j = 0, 0

    while row > 1 and col > 1:
        l = collections.deque()
        for k in range(col-1):
            l.append(matrix[i][j+k])
        for k in range(row-1):
            l.append(matrix[i+k][j+col-1])
        for k in range(col-1, 0, -1):
            l.append(matrix[i+row-1][j+k])
        for k in range(row-1, 0, -1):
            l.append(matrix[i+k][j])

        l.rotate(-R)

        for k in range(col-1):
            matrix[i][j+k] = l.popleft()
        for k in range(row-1):
            matrix[i+k][j+col-1] = l.popleft()
        for k in range(col-1, 0, -1):
            matrix[i+row-1][j+k] = l.popleft()
        for k in range(row-1, 0, -1):
            matrix[i+k][j] = l.popleft()

        row, col = row-2, col-2
        i, j = i+1, j+1

    for i in range(M):
        print(' '.join(str(v) for v in matrix[i]))
