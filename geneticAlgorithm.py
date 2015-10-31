"""
This file contains the Genetic algorithm based functions and modules for the player
"""
import numpy as np
from helpers import random_number
import random
from neural_net import NeuralNet
from tic_tac_toe import play_game
import copy
import matplotlib.pyplot as plt
import matplotlib


MUTATION_RATE = 0.5
POPULATION_SIZE = 100
MAX_GENERATIONS = 50
CROSSOVER_RATE = 0.5

WIN_SCORE = 1.0
LOSS_SCORE = -6.0
DRAW_SCORE = 0.0


class GeneticAlgorithm:
    def __init__(self):
        self.population = [NeuralNet() for ix in xrange(POPULATION_SIZE)]
        self.generation = 1

    def sort_fitness(self):
        self.population = sorted(self.population, key=lambda x: x.fitness, reverse=True)
    
    def evolve_and_plot_weights(self):
        best_player_across_generations = NeuralNet()
        best_fitness_across_generations = -100
        current_gen = 1
        while current_gen <= MAX_GENERATIONS:

            for p in self.population:
                p.fitness = self.calculate_fitness(p)
            self.sort_fitness()

            best_player = self.population[0]
            if best_player.fitness > best_fitness_across_generations:
                best_fitness_across_generations = best_player.fitness
                best_player_across_generations = copy.deepcopy(best_player)
            print "Current generation: " + str(current_gen) + " , best fitness: " + str(best_player.fitness)
            plt.subplot(1, 3, 1)
            plt.pcolor(best_player.W1)
            plt.subplot(1, 3, 2)
            plt.pcolor(best_player.W2)
            plt.subplot(1, 3, 3)
            plt.pcolor(best_player.W3)
            plt.show()

            temp = []
            while len(temp) < POPULATION_SIZE:
                offspring_one = self.population[self.selection_function()]
                offspring_two = self.population[self.selection_function()]

                offspring_one.CHROMOSOME, offspring_two.CHROMOSOME = self.crossover(offspring_one.CHROMOSOME,
                                                                                    offspring_two.CHROMOSOME)

                offspring_one.CHROMOSOME = self.mutate(offspring_one.CHROMOSOME)
                offspring_two.CHROMOSOME = self.mutate(offspring_two.CHROMOSOME)

                temp.append(offspring_one)
                temp.append(offspring_two)
            self.population, temp = temp, self.population
            current_gen += 1

    def evolve(self):
        best_player_across_generations = NeuralNet()
        best_fitness_across_generations = -100
        current_gen = 1
        while current_gen <= MAX_GENERATIONS:

            for p in self.population:
                p.fitness = self.calculate_fitness(p)
            self.sort_fitness()

            best_player = self.population[0]
            if best_player.fitness > best_fitness_across_generations:
                best_fitness_across_generations = best_player.fitness
                best_player_across_generations = copy.deepcopy(best_player)
            print "Current generation: " + str(current_gen) + " , best fitness: " + str(best_player.fitness)

            temp = []
            while len(temp) < POPULATION_SIZE:
                offspring_one = self.population[self.selection_function()]
                offspring_two = self.population[self.selection_function()]

                offspring_one.CHROMOSOME, offspring_two.CHROMOSOME = self.crossover(offspring_one.CHROMOSOME,
                                                                                    offspring_two.CHROMOSOME)

                offspring_one.CHROMOSOME = self.mutate(offspring_one.CHROMOSOME)
                offspring_two.CHROMOSOME = self.mutate(offspring_two.CHROMOSOME)

                temp.append(offspring_one)
                temp.append(offspring_two)
            self.population, temp = temp, self.population
            current_gen += 1

        # When evolution has stopped
        print best_player_across_generations.fitness, best_fitness_across_generations
        # print best_player_chromosome_across_generations
        # Save the best generation Genome in a file
        f = open("./player_genomes/best_genome.txt", 'w')
        f.write("fitness "+str(best_player_across_generations.fitness)+"\n")
        f.write("NX "+str(best_player_across_generations.NX)+"\n")
        f.write("N1 "+str(best_player_across_generations.N1)+"\n")
        f.write("N1 "+str(best_player_across_generations.N2)+"\n")
        f.write("NY "+str(best_player_across_generations.NY)+"\n")

        for ch_ix in best_player_across_generations.CHROMOSOME:
            f.write(str(ch_ix)+"\n")
        f.close()

    def calculate_fitness(self, player):
        """
        play a match for NN player vs. random player and assign fitness depending on the result of the match/matches
        number of matches to play = 1
        play only as player 1 for some time.
        TODO: play as player 1 and player 2 to calculate total fitness.
        :param player: The selected neural network player
        :return: the score from the resulting match/matches
        """

        wins, losses, draws = play_game(player, 1)  # playing as player 1

        player.fitness = (WIN_SCORE * wins + LOSS_SCORE * losses + DRAW_SCORE * draws) / (wins + losses + draws)
        return player.fitness

    def selection_function(self):
        """
        select best players from the population based on Roulette wheel selection Algorithm.
        :return: the index of the selected player
        """
        return random.randint(0, len(self.population) / 4)

    def crossover(self, offspring1, offspring2):
        """
        perform a crossover on the offspring and return the changed offsprings with new chromosomes
        :param offspring1: first NN player
        :param offspring2: second NN player
        :return: new offsprings generated
        """
        # if random_number() < CROSSOVER_RATE:
        #     crossover_val = int(random_number() * len(offspring1))
        #     t1 = offspring1[:crossover_val] + offspring2[crossover_val:]
        #     t2 = offspring2[:crossover_val] + offspring1[crossover_val:]

        # Changing the way we do crossovers
        for c_ix in range(len(offspring1)):
            if random_number() < CROSSOVER_RATE:
                offspring1[c_ix], offspring2[c_ix] = offspring2[c_ix], offspring1[c_ix]

        #     return t1, t2
        return offspring1, offspring2

    def mutate(self, chromo):
        """
        Function takes chromosome inputs and mutates the chromosome based on mutation rate
        :param chromo: input player chromosome
        :return: mutated player chromosome
        """
        for z in xrange(len(chromo)):

            if random_number() < MUTATION_RATE:
                chromo[z] = random_number()
        return chromo

    def change_weights(self, player):
        player.W1 = np.reshape(np.asarray(player.CHROMOSOME[:(player.NX * player.N1)]), (player.NX, player.N1))
        player.W2 = np.reshape(np.asarray(player.CHROMOSOME[(player.NX * player.N1):(player.N1 * player.N2)]),
                               (player.N1, player.N2))
        player.W3 = np.reshape(np.asarray(player.CHROMOSOME[(player.N2 * player.NY):]), (player.N2, player.NY))


if __name__ == '__main__':
    ga = GeneticAlgorithm()
    print "Initializing ... "
    ga.evolve()
