from functools import reduce
from operator import mul, sub

def column(row):
    i = 0
    n = len(row)
    while not row[i] and i < n:
        i += 1
    return i if i < n else -1

def sign(indexes):
    s = sum((0, 1)[x < y] for k, y in enumerate(indexes) for x in indexes[k+1:])
    return ((s + 1) % 2 - s % 2)

def det(matrix):
    M = matrix[:]
    n = len(M)

    indexes = [0 for _ in range(n)]

    for i in range(n):
        k = column(M[i])
        for j in (x for x in range(n) if x != i):
            M[j] = tuple(map(sub, M[j],
                             map(mul, M[i], [M[j][k] / M[i][k]] * (n+1))))
        indexes[i] = k

    return reduce(mul, (M[i][indexes[i]] for i in range(n)), 1) * sign(indexes)

def gauss(les):

    n = len(les)
    M = les[:]

    indexes = [0 for _ in range(n)]

    for i in range(n):
        k = column(M[i])
        M[i] = [M[i][j] / M[i][k] for j in range(n+1)]
        for j in (x for x in range(n) if x != i):
            M[j] = tuple(map(sub, M[j], map(mul, M[i], [M[j][k]] * (n + 1))))
        indexes[i] = k

    return [M[indexes[i]][n] for i in range(n)]

if "__main__" == __name__:
    matrix = [(2,5,4,1,20),(1,3,2,1,11),(2,10,9,7,40),(3,8,9,2,37)]
    print(gauss(matrix))



