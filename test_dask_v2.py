from time import time


N = 10 ** 6

def square(x):
	return x ** 2

def divide(x):
	return x / N

from random import random

from dask.distributed import Client
client = Client(processes=False)
import dask.bag as db

start = time()

A = db.from_sequence(range(N)).map(lambda x: random())
B = A.map(square)
C = B.map(divide)
D = C.sum().compute()
print(D)

end = time()
print('  dask:', end - start)


start = time()

A = [random() for _ in range(N)]
B = map(square, A)
C = map(divide, B)
D = sum(C)
print(D)

end = time()
print('no dask:', end - start)

