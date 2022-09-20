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
    healthy_clr = "b"
    infected_clr = "r"
    recovered_clr = "g"
    dead_clr = "k"

    # put label in graph
    plt.plot(0, all_runs[0][0][1], healthy_clr, label="Healthy")
    plt.plot(0, all_runs[0][0][2], infected_clr, label="Infected")
    plt.plot(0, all_runs[0][0][3], recovered_clr, label="Recovered")
    plt.plot(0, all_runs[0][0][4], dead_clr, label="Dead")


    for i in range(runs):
        # y.append([])
        # y[i] = all_runs[i][:, 1] #living population
        plt.plot(x, all_runs[i][:, 1], healthy_clr) #, label="Healthy"
        plt.plot(x, all_runs[i][:, 2], infected_clr) #, label="Infected"
        plt.plot(x, all_runs[i][:, 3], recovered_clr) #, label="Recovered"
        plt.plot(x, all_runs[i][:, 4], dead_clr) #, label="Dead"

    plt.legend()
    plt.show()

def find_peak_infections(all_runs):
    """returns a list of highest infections, and the times for each simulation"""
    print(len(all_runs))
    sim_len = all_runs[0][-1][0].item() + 1  #time of last entry in time col of first run
    output = np.empty([len(all_runs), 2], dtype=int)
    for i in range(len(all_runs)):
        max = 0
        time = 0
        for j in range(sim_len):
            # print("i, j", i, j)
            # print(type(all_runs[i][j][2]))
            if (all_runs[i][j][2].item() > max):
                max = all_runs[i][j][2].item()
                time = all_runs[i][j][0].item()
            # print(type(i), type(j))

        output[i][0] = max
        output[i][1] = time

        # for j in np.nditer(all_runs[i][:, 2]):
        #     if (j > max)


        # np.append(output, [max, time])
    # print("peaks are ", output)

    return output


    # pass




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

    print(all_runs[0][:, 2])

    print(find_peak_infections(all_runs))

    # for j in np.nditer(all_runs[0][:, 1]):
    #     print(j)

    # print(len(all_runs[1][:, 1]))
    # print(type(all_runs[0][-1][0]))
    # print(type(all_runs[0][-1][0].item()))
    # graph_populations(runs, all_runs)




























if __name__ == '__main__':
    main()
