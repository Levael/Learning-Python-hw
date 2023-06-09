import random


def CalculateFrobeniusNorm (matrix):
    pre_frobenius_norm = 0

    for vector in matrix:
        for value in vector:
            pre_frobenius_norm += value**2

    frobenius_norm = pre_frobenius_norm**0.5
    return frobenius_norm


def CalculateOperatorNorm (matrix):
    return max(list(map(lambda arr: sum(arr), matrix)))


def GetMatrixNorm1_2x2 ():
    # from 0 to 1
    x1 = random.random()
    x2 = random.random()

    return [[x1, (1-x1**2)**0.5], [x2, (1-x2**2)**0.5]]


def GetMatrix_nxn (n = 3, max_x = 5):
    # makes two-dimensional list
    matrix = [[0] * n for i in range(n)]

    for vector in range(n):
        for value in range(n):
            matrix[vector][value] = random.random()*max_x

    return matrix


print(CalculateOperatorNorm(GetMatrixNorm1_2x2()))
print(CalculateFrobeniusNorm(GetMatrix_nxn()))
