from time import time


N = 10 ** 4

def square(x):
	return x ** 2

def divide(x):
	return x / N

from random import random as rnd
def random(_):
	return rnd()


from dask.distributed import Client
client = Client(processes=False)

start = time()

A = client.map(random, range(N))
B = client.map(square, A)
C = client.map(divide, B)
D = client.submit(sum, C)
print(D.result())

end = time()
print('  dask:', end - start)


start = time()

A = map(random, range(N))
B = map(square, A)
C = map(divide, B)
D = sum(C)
print(D)

end = time()
print('no dask:', end - start)

