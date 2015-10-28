import numpy as np
import matplotlib.pyplot as plt
import random

nx = 9
n1 = 10
n2 = 10
ny = 1

# w1 = np.zeros((nx, n1))
# w2 = np.zeros((n2, n1)).T
# w3 = np.zeros((n2, 1))
ix = 0
sum_val = 0
N = 100
min_val = 10000
max_val = -10000
ll = []
while ix < N:
    ix += 1
    w1 = np.random.rand(nx, n1)
    w2 = np.random.rand(n2, n1)
    w3 = np.random.rand(n2, 1)

    # x = np.zeros((nx, 1))
    # l1 = np.zeros((1, n1))
    # l2 = np.zeros((1, n2))

    inp = [0, 0, 1, 1, -1, -1, 0, 0, 0]
    # x = np.random.rand(nx, 1)
    x = np.asarray(inp)
    x = np.reshape(x, (1, len(inp)))


    # l1 = np.random.rand(1, n1)
    # l2 = np.random.rand(1, n2)


    # print w1
    # print w2
    # print w3
    # print x
    # print l1
    # print l2

    def sigmoid(x):
        return 5.0 / (1 + np.exp(-1 * x))


    l1 = np.dot(x, w1)
    # l1 = sigmoid(l1)
    l1 = np.tanh(l1) + random.random()
    l2 = np.dot(l1, w2.T)
    # l2 = sigmoid(l2)
    l2 = np.tanh(l2) + random.random()
    y = np.dot(l2, w3)
    # y = sigmoid(y)
    # y = np.tanh(y)
    y_val = abs(np.round(9 * y / 15))
    sum_val += y_val
    ll.append(y_val)
    if y_val < min_val:
        min_val = y_val

    if y_val > max_val:
        max_val = y_val


# print np.round(sum_val/N)
print min_val, max_val

for i in range(10):
    print i, "::::", ll.count(i)
