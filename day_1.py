# matrix = [
#     [
#         [1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#         [13, 14, 15, 16]
#     ],
#     [
#         [17, 18, 19, 20],
#         [21, 22, 23, 24],
#         [25, 26, 27, 28],
#         [29, 30, 31, 32]
#     ],
#     [
#         [33, 34, 35, 36],
#         [37, 38, 39, 40],
#         [41, 42, 43, 44],
#         [45, 46, 47, 48]
#     ],
#     [
#         [49, 50, 51, 52],
#         [53, 54, 55, 56],
#         [57, 58, 59, 60],
#         [61, 62, 63, 64]
#     ]
# ]

# new = [[[matrix[k][i][j] for i in range(4)] for j in range(4)] for k in range(4)]


# for j in range(4):
#     for k in range(4):
#         new.append(matrix[k][j][i])


import numpy as np
import random
from funct import cvmatrix

#  CREATE REGULAR LIST
# number_list = [i for i in range(1, 65)]
# matrix_1 = np.array(number_list)
# four_dimensional = matrix_1.reshape(4, 4, 4)
# new_matrix = cvmatrix(four_dimensional)
# print(new_matrix)


#  CREATE REGULAR LIST 1-64
# random_list = [random.randint(1,100) for i in range(1, 65)] # with loop
# random_list = random.sample(range(1, 100), 64) # without loop
# matrix_1 = np.array(random_list)
# four_dimensional = matrix_1.reshape(4, 4, 4)
# new_matrix = cvmatrix(four_dimensional)
# print(new_matrix)
