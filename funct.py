# Clockwise turn matrix

def cvmatrix(matrix):
    return [[[matrix[k][i][j] for i in range(4)] for j in range(4)] for k in range(4)]