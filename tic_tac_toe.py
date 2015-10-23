import random

PLAYER = 0


class Game:
    board = [[], [], []]

    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def play(self, index, player):
        x = int(index / 3)
        y = int(index % 3)
        if self.board[x][y] == 0:
            self.board[x][y] = player

    def linear_board(self):
        b = []
        for i in self.board:
            for j in i:
                b.append(j)

        return b

    def available_moves(self):
        brd = self.linear_board()
        av = []
        for x in range(len(brd)):
            if brd[x] == 0:
                av.append(x)

        return av

    def check_status(self):

        # check status for win on the board
        for i in self.board:
            sum_ = 0
            for j in i:
                sum_ += j
            if abs(sum_) == 3:
                # we have a winner
                return int(sum_ / 3)

        # check vertically
        for i in range(3):
            sum_ = 0
            for j in range(3):
                sum_ += self.board[j][i]
            if abs(sum_) == 3:
                # we have a vertical winner
                return int(sum_ / 3)

        # check diagonally
        sum_ = 0
        for i in range(3):
            sum_ += self.board[i][i]
        if abs(sum_) == 3:
            # we have a front diagonal winner
            return int(sum_ / 3)

        sum_ = self.board[2][0] + self.board[1][1] + self.board[0][2]
        if abs(sum_) == 3:
            # last check for winner
            return int(sum_ / 3)

        # check draw if game ended
        for i in self.board:
            for j in i:
                if j == 0:
                    # The game hasn't ended yet
                    return 10
        # The game has ended with a draw
        return 0


if __name__ == '__main__':
    PLAYER = 1
    for i in range(10):
        PLAYER = 1
        game = Game()
        while game.check_status() == 10:  # The game continues
            av = game.available_moves()
            # print av
            move = random.choice(av)
            # print move, "MOVE"
            game.play(move, PLAYER)
            status = game.check_status()
            if status == 1:
                print "Player 1 has won"
            elif status == -1:
                print "Player 2 has won"
            elif status == 0:
                print "Game was a draw"
            PLAYER *= -1
