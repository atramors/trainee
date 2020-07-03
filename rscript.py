import requests
from funct import crmatrix_norm
import numpy as np


def crmatrix_norm():
    number_list = [i for i in range(1, 16001)]
    matrix_1 = np.array(number_list)
    matrix_1 = matrix_1.reshape(1000, 4, 4)
    return matrix_1.tolist()

for i in range(21):
    res = requests.post("http://127.0.0.1:5000/", json={"data": crmatrix_norm()})
    print(res.status_code)
