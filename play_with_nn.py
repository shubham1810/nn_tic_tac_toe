import numpy as np
from neural_net import NeuralNet
from tic_tac_toe import Game
import random


def parse_genome(data):
    fitness = float(data[0].split(' ')[1])
    nx = int(data[1].split(' ')[1])
    n1 = int(data[2].split(' ')[1])
    n2 = int(data[3].split(' ')[1])
    ny = int(data[4].split(' ')[1])

    print nx, n1, n2,  ny

    w1 = np.asarray(data[5:5+int(nx*n1)]).astype(np.float)
    w2 = np.asarray(data[5+int(nx*n1):5+int(nx*n1)+int(n1*n2)]).astype(np.float)
    w3 = np.asarray(data[5+int(nx*n1)+int(n1*n2):]).astype(np.float)

    return w1, w2, w3, nx, n1, n2, ny, fitness


def play_a_game(nn_player, player_type):
    p1 = 0
    p2 = 0
    n = 1
    for i in range(n):
        PLAYER = 1
        game = Game()
        while game.check_status() == 10:  # The game continues
            av = game.available_moves()
            # print av
            if PLAYER == player_type:
                print "NN is playing..."
                move = nn_player.forward_pass(game.linear_board())
                # print move
            else:
                print av
                move = input() - 1
                # move = random.choice(av)
            # print move, "MOVE"
            game.play(move, PLAYER)
            status = game.check_status()
            if status == 1:
                # print "Player 1 has won"
                p1 += 1
            elif status == -1:
                # print "Player 2 has won"
                p2 += 1
            elif status == 0:
                # print "Game was a draw"
                pass
            PLAYER *= -1
            board_current = game.linear_board()
            print board_current[0:3]
            print board_current[3:6]
            print board_current[6:9]
    wins = p1
    losses = p2
    draws = n - (wins + losses)
    return wins, losses, draws


if __name__ == '__main__':
    f = open("player_genomes/best_genome.txt", 'rb').read()
    data = f.split('\n')[:-1]
    w1, w2, w3, nx, n1, n2, ny, fit = parse_genome(data)
    nn_p = NeuralNet()
    nn_p.load_from_genome(w1, w2, w3, nx, n1, n2, ny, fit)
    print play_a_game(nn_p, 1)
'''
[X - X]
[X O -]
[O - O]'''