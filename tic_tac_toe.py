import random


class Game:

    board = [[], [], []]

    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def play(self, x, y, player):
        if self.board[x][y] is not 0:
            self.board[x][y] = player

    def check_status(self):

        # check status for win on the board
        for i in self.board:
            sum_ = 0
            for j in i:
                sum_ += j
            if abs(sum_) == 3:
                # we have a winner
                return int(sum_/3)

        # check vertically
        for i in range(3):
            sum_ = 0
            for j in range(3):
                sum_ += self.board[j][i]
            if abs(sum_) == 3:
                # we have a vertical winner
                return int(sum_/3)

        # check diagonally
        sum_ = 0
        for i in range(3):
            sum_ += self.board[i][i]
        if abs(sum_) == 3:
            # we have a front diagonal winner
            return int(sum_/3)

        sum_ = self.board[2][0] + self.board[1][1] + self.board[0][2]
        if abs(sum_) == 3:
            # last check for winner
            return int(sum_/3)

        # check draw if game ended
        for i in self.board:
            for j in i:
                if j == 0:
                    # The game hasn't ended yet
                    return 10
        # The game has ended with a draw
        return 0


if __name__ == '__main__':
    pass
