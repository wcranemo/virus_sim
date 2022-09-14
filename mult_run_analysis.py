"""

Description: takes data from multiple runs of same parameter values
and plots and analyzes them.
"""

import sys
# import pandas as pd
# from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt


def graph_populations(runs, all_runs):
    x = all_runs[0][:, 0]
    # y = []


    for i in range(runs):
        # y.append([])
        # y[i] = all_runs[i][:, 1] #living population
        plt.plot(x, all_runs[i][:, 1], 'b', label="Healthy")
        plt.plot(x, all_runs[i][:, 2], 'r', label="Infected")
        plt.plot(x, all_runs[i][:, 3], 'g', label="Recovered")
        plt.plot(x, all_runs[i][:, 4], 'k', label="Dead")

    # plt.legend()
    plt.show()



def main():
    """ main function """

    print("running this badboy")

    runs = int(input())

    # print(type(runs))
    # print(runs)

    all_runs = []

    for i in range(runs):
        all_runs.append([])
        # print(type(i))

        # print("i = ", i)
        data = np.genfromtxt(f'out{i + 1}.txt', dtype=int, delimiter=',', skip_header=1, #skips the header line
            autostrip=False)
        data = np.delete(data, 5, 1) #delete excess column
        all_runs[i] = data

    # print(all_runs[0], "\n")
    # print()
    # print(all_runs[runs - 1])
    # print(all_runs[0][:, 0])
    # print(all_runs[0, :, 0])
    # print(all_runs)
    # print(all_runs[0][:, 0])
    # print(all_runs[0][:, 1])
    # print(all_runs[1][:, 1])

    graph_populations(runs, all_runs)




























if __name__ == '__main__':
    main()
