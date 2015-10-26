"""
Neural Network Class to save data about the net and train the player

chromosome will be as follows:
the chromosome is a 2D matrix

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
import random


class NeuralNet:

    def __init__(self):
        self.NX = 9
        self.LAYERS = 2
        self.N1 = 10
        self.N2 = 10
        self.NY = 1
        self.X = np.zeros(self.NX)
        self.W1 = np.zeros((self.NX, self.N1))
        self.L1 = np.zeros((self.N2, self.N1))
        self.W2 = np.zeros((self.N1, ))
        self.L2 = []
        self.W3 = []
        self.Y = []

        # create a weight matrix
        self.weights = []

        for i in range(self.LAYERS):
            pass


if __name__ == '__main__':
    print np
