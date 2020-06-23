
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

new = [[[matrix[k][i][j] for i in range(4)] for j in range(4)] for k in range(4)]


    # for j in range(4):
    #     new.append(matrix[0][j][0])
    # new.append(matrix[0][0][i])
    


    # for j in range(4):
    #     for k in range(4):
    #         new.append(matrix[k][j][i])

# b = np.matrix(new, dtype=np.int32)
# c = [[[matrix[k][j][i] for k in xrange(n)] for j in xrange(n)] for i in xrange(n)]
strin = "{'qwer': 1, 'qwe': 2}, {'rte': 3}"
# print(dir(strin))
print(strin.split(','))