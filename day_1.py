matrix = [
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ],
    [
        [17, 18, 19, 20],
        [21, 22, 23, 24],
        [25, 26, 27, 28],
        [29, 30, 31, 32]
    ],
    [
        [33, 34, 35, 36],
        [37, 38, 39, 40],
        [41, 42, 43, 44],
        [45, 46, 47, 48]
    ],
    [
        [49, 50, 51, 52],
        [53, 54, 55, 56],
        [57, 58, 59, 60],
        [61, 62, 63, 64]
    ]
]

# new = [[[matrix[k][i][j] for i in range(4)] for j in range(4)] for k in range(4)]


# for j in range(4):
#     for k in range(4):
#         new.append(matrix[k][j][i])


# import numpy as np
# import random
# from funct import cwmatrix

#  CREATE REGULAR LIST
# number_list = [i for i in range(1, 65)]
# matrix_1 = np.array(number_list)
# four_dimensional = matrix_1.reshape(4, 4, 4)
# new_matrix = cwmatrix(four_dimensional)
# print(new_matrix)


# # print(number_list)
# print(matrix_1)
# print(four_dimensional[0][0])


#  CREATE LIST OF RANDOM NUMBERS 1-64
# random_list = [random.randint(1,100) for i in range(1, 65)] # with loop
# random_list = random.sample(range(1, 100), 64) # without loop
# matrix_1 = np.array(random_list)
# four_dimensional = matrix_1.reshape(4, 4, 4)
# new_matrix = cwmatrix(four_dimensional)
# print(new_matrix)

A = matrix
B = matrix


# def matrixmult(A, B):       
#     return [[[[sum(A[m_num][row][elem] * B[m_num][elem][col]) for elem in range(4)] for col in range(4)] for row in range(4)] for m_num in range(4)]
          

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

# print(matrixmult(A, B))

