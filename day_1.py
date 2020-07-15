mat = [
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
    [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]],
    [[33, 34, 35, 36], [37, 38, 39, 40], [41, 42, 43, 44], [45, 46, 47, 48]],
    [[49, 50, 51, 52], [53, 54, 55, 56], [57, 58, 59, 60], [61, 62, 63, 64]],
]

# new = [[[matrix[k][i][j] for i in range(4)] for j in range(4)] for k in range(4)]

# for j in range(4):
#     for k in range(4):
#         new.append(matrix[k][j][i])


# A = B = mat

# def matrixmult(A, B):
#     length = range(len(A))
#     row = column = numbers = range(4)
#     return [[[sum(A[l][r][n] * B[l][n][c] for n in numbers)for c in column]for r in row]for l in length]

# print(matrixmult(A, B))

# import random
# import numpy as np

# def cwmatrix(matrix):
#     length = range(len(matrix))
#     row = column = range(4)
#     return [[[matrix[l][c][r] for c in column] for r in row] for l in length]

# def crmatrix_rand():
#     # random_list = [random.randint(1,100) for i in range(1, 65)] # with loop
#     random_list = random.sample(range(1, 65), 64)  # without loop
#     matrix_1 = np.array(random_list)
#     matrix_1 = matrix_1.reshape(4, 4, 4)
#     return matrix_1.tolist()

# A = crmatrix_rand()

# print(A)
# print()
# print(cwmatrix(A))
def x(i):
    return i**2

lis = [1,2,3,4,5]
sq = list(map(x, lis))
print(sq)