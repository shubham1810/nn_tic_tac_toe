"""
Neural Network Class to save data about the net and train the player

chromosome will be as follows:
the chromosome is a 2D matrix
TODO: Change the matrix structure in this diagram for the New NN structure
        | [<------------ l1 + 1 ------------>]
        | [                            |  0  ]
        | [                            |  0  ]
        | [              W1            |  0  ]
        | [                            |  0  ]
        | [                            |  0  ]
   (9+l2) [----------------------------|- 1 -]
        | [                            |     ]
        | [                            |     ]
        | [              W2            |  W3 ]
        | [                            |     ]
        | [                            |     ]
        | [                            |     ]

"""
import numpy as np
from helpers import softmax


class NeuralNet:
    def __init__(self):
        self.NX = 9
        self.LAYERS = 2
        self.N1 = 10
        self.N2 = 10
        self.NY = 9
        self.X = np.zeros(self.NX)
        # self.W1 = np.zeros((self.NX, self.N1))
        self.W1 = np.random.rand(self.NX, self.N1)
        self.L1 = np.zeros((1, self.N1))
        # self.W2 = np.zeros((self.N2, self.N1))
        self.W2 = np.random.rand(self.N2, self.N1)
        self.L2 = np.zeros((1, self.N2))
        # self.W3 = np.zeros((self.N2, self.NY))
        self.W3 = np.random.rand(self.N2, self.NY)
        self.Y = np.zeros((1, self.NY))
        self.activation = np.zeros((1, self.NX))
        self.y_out = []
        self.OUT = 0
        self.fitness = 0

    def forward_pass(self, inp):

        for ix in range(len(inp)):
            if inp[ix] == 0:
                self.activation[0][ix] = 1
            else:
                self.activation[0][ix] = 0

        self.X = self.activation
        self.L1 = np.tanh(np.dot(self.X, self.W1))
        self.L2 = np.tanh(np.dot(self.L1, self.W2.T))
        self.Y = softmax(np.dot(self.L2, self.W3))
        self.y_out = []
        for ix in range(self.Y.shape[1]):
            self.y_out.append(self.Y[0][ix] * self.activation[0][ix])
        self.OUT = np.argmax(self.y_out)
        return self.OUT


if __name__ == '__main__':
    nn = NeuralNet()
    print nn.forward_pass([0, 0, 0, 0, 0, 0, 0, 0, 0])
