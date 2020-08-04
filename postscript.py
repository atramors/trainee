import aiohttp
import asyncio
import random
import requests
import time
import numpy as np
from profilehooks import profile, timecall


def crmatrix_norm():
    number_list = [i for i in range(1, 65)]
    matrix_1 = np.array(number_list)
    matrix_1 = matrix_1.reshape(4, 4, 4)

    return matrix_1.tolist()


def crmatrix_rand():
    random_list = random.sample(range(1, 65), 64)
    matrix_1 = np.array(random_list)
    matrix_1 = matrix_1.reshape(4, 4, 4)

    return matrix_1.tolist()


# for i in range(10):
#     res = requests.post("http://127.0.0.1:5000/", json={"data": crmatrix_norm()})
# print(res.status_code)
res = requests.post("http://127.0.0.1:5000/", json={"data": crmatrix_norm()})

# class Coro1(object):
#     def __await__(self):
#         a = yield requests.post("http://127.0.0.1:5000/", json={"data": crmatrix_norm()})# Obtain sent value
#         return a # Return computed vaue back

# async def coro2():
#     for i in range(10):
#         b = await Coro1() # Get return value from Coro1 instance
#         print(b.status_code) # Return computed value further upward to pipeline

#########################
# async def req():
#     return requests.post("http://127.0.0.1:5000/", json={"data": crmatrix_norm()})


# async def loo():
#     for i in range(10):
#         print(i)
#         await asyncio.create_task(req())


# @timecall
# def a():
#     return asyncio.run(loo())


# a()


# @timecall
# def b():
#     for i in range(10):
#         print(i)
#         requests.post("http://127.0.0.1:5000/", json={"data": crmatrix_norm()})

# b()


# async def req():
#     return requests.post("http://127.0.0.1:5000/", json={"data": crmatrix_norm()})


# async def loo():
#     for i in range(10):
#         await req()

# @timecall
# def c():
#     return asyncio.run(loo())
# c()

###########################
# @profile
# def asyn():
#     asyncio.run(coro2())

# asyn()

