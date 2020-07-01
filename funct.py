import numpy as np
import random
import cProfile
from profilehooks import profile


@profile(immediate=True)
def cwmatrix(matrix):
    return [[[matrix[k][i][j] for i in range(4)] for j in range(4)] for k in range(4)]


# Create regular 3-dimensional matrix

@profile(immediate=True)
def crmatrix_norm():
    number_list = [i for i in range(1, 65)]
    matrix_1 = np.array(number_list)
    return matrix_1.reshape(4, 4, 4)


# Create random 3-dimensional matrix

@profile(immediate=True)
def crmatrix_rand():
    # random_list = [random.randint(1,100) for i in range(1, 65)] # with loop
    random_list = random.sample(range(1, 100), 64)  # without loop
    matrix_1 = np.array(random_list)
    return matrix_1.reshape(4, 4, 4)


# Multiplication of 2 matrices

# For loops

# def matrixmult(A, B):
#     C = []
#     for m_num in range(4):
#         matrix_ = []
#         for row in range(4):
#             column = []
#             for col in range(4):
#                 element = 0
#                 for elem in range(4):
#                     element += A[m_num][row][elem] * B[m_num][elem][col]
#                 column.append(element)
#             matrix_.append(column)
#         C.append(matrix_)
#     return C

# List comprehension

# A = crmatrix_norm()
# B = crmatrix_rand()

@profile(immediate=True)
def matrixmult(A, B):
    return [
        [
            [
                sum(A[m_num][row][elem] * B[m_num][elem][col] for elem in range(4))
                for col in range(4)
            ]
            for row in range(4)
        ]
        for m_num in range(4)
    ]
# matrixmult(A, B)
# cProfile.run('matrixmult(A,B)')