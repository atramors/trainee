import numpy as np
import random

# Clockwise turn matrix


def cwmatrix(matrix):
    return [[[matrix[k][i][j] for i in range(4)] for j in range(4)] for k in range(4)]


# Create regular 3-dimensional matrix


def crmatrix_norm():
    number_list = [i for i in range(1, 65)]
    matrix_1 = np.array(number_list)
    four_dimensional = matrix_1.reshape(4, 4, 4)
    return four_dimensional


# Create random 3-dimensional matrix


def crmatrix_rand():
    # random_list = [random.randint(1,100) for i in range(1, 65)] # with loop
    random_list = random.sample(range(1, 100), 64)  # without loop
    matrix_1 = np.array(random_list)
    four_dimensional = matrix_1.reshape(4, 4, 4)
    return four_dimensional


print(crmatrix_rand())
print(crmatrix_norm())
