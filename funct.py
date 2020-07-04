import numpy as np
import random
import cProfile
from profilehooks import profile


@profile(sort="cumtime")
def cwmatrix(matrix):
    length = range(len(matrix))
    row = column = range(4)
    return [[[matrix[l][c][r] for c in column] for r in row] for l in length]


# Create regular 3-dimensional matrix

# @profile
def crmatrix_norm():
    number_list = [i for i in range(1, 65)]
    matrix_1 = np.array(number_list)
    return matrix_1.reshape(4, 4, 4)


# Create random 3-dimensional matrix

# @profile
def crmatrix_rand():
    # random_list = [random.randint(1,100) for i in range(1, 65)] # with loop
    random_list = random.sample(range(1, 65), 64)  # without loop
    matrix_1 = np.array(random_list)
    return matrix_1.reshape(4, 4, 4)


# MULTIPLICATION OF MATRICES

# For loops

# def matrixmult(A, B):
#     C = []
#     length = range(len(A))
#     row = column = numbers = range(4)
#     for l in length:
#         rows = []
#         for r in row:
#             columns = []
#             for c in column:
#                 element = 0
#                 for n in numbers:
#                     element += A[l][r][n] * B[l][n][c]
#                 columns.append(element)
#             rows.append(columns)
#         C.append(rows)
#     return C

# List comprehension

# @profile
def matrixmult(A, B):
    length = range(len(A))
    row = column = numbers = range(4)
    return [
        [[sum(A[l][r][n] * B[l][n][c] for n in numbers) for c in column] for r in row]
        for l in length
    ]


# @profile(sort="cumtime")
# def matrixmult3d(A, B):
#     C = []
#     dimension1 = range(len(A))
#     dimension2 = dimension3 = range(4)
#     for r in dimension1:
#         column = []
#         for c in dimension2:
#             element = 0
#             for n in dimension3:
#                 element += A[r][n] * B[n][c]
#             column.append(element)
#         C.append(column)
#     return C


@profile(sort="cumtime")
def matrixmult3d(A, B):
    dimension1 = range(len(A))
    dimension2 = dimension3 = range(4)

    return [
        [sum(A[r][n] * B[n][c] for n in dimension3) for c in dimension2]
        for r in dimension1
    ]
