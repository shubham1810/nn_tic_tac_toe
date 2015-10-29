import numpy as np
import matplotlib.pyplot as plt
import random

nx = 9
n1 = 10
n2 = 10
ny = 9

# w1 = np.zeros((nx, n1))
# w2 = np.zeros((n2, n1)).T
# w3 = np.zeros((n2, 1))
ix = 0
sum_val = 0
N = 100
min_val = 10000
max_val = -10000
ll = []

ix += 1
w1 = np.random.rand(nx, n1)
w2 = np.random.rand(n2, n1)
w3 = np.random.rand(n2, ny)

# x = np.zeros((nx, 1))
# l1 = np.zeros((1, n1))
# l2 = np.zeros((1, n2))

inp = [-1, 1, 1,
       1, -1, -1,
       1, -1, 1]

activation = []
for i in inp:
    if i == 0:
        activation.append(1)
    else:
        activation.append(0)
print activation

# x = np.random.rand(nx, 1)
x = np.asarray(activation)
x = np.reshape(x, (1, len(inp)))
print x.shape

# print w1
# print w2
# print w3
# print x
# print l1
# print l2


def sigmoid(z):
    return 5.0 / (1 + np.exp(-1 * z))


l1 = np.dot(x, w1)
# l1 = sigmoid(l1)
l1 = np.tanh(l1)
l2 = np.dot(l1, w2.T)
# l2 = sigmoid(l2)
l2 = np.tanh(l2)
y = np.dot(l2, w3)
y = (np.exp(y))/(np.sum(np.exp(y)))  # softmax
y_out = []
for ix in range(y.shape[1]):
    y_out.append(y[0][ix] * activation[ix])
print y_out
print np.argmax(y_out)

