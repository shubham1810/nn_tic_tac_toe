"""
A collection of helper functions for Neural Network and Genetic Algorithm based training.
"""
import numpy as np
import random


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-1 * z))


def softmax(z):
    return np.exp(z) / np.sum(np.exp(z))


def random_number():
    return random.random()


if __name__ == '__main__':
    pass
