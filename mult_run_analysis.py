"""

Description: takes data from multiple runs of same parameter values
and plots and analyzes them.
"""

import sys
# import pandas as pd
# from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


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
            if (all_runs[i][j][2].item() > max):
                max = all_runs[i][j][2].item()
                time = all_runs[i][j][0].item()

        output[i][0] = max
        output[i][1] = time

    return output


    # pass

def graph_peak_infections(all_runs):
    """outputs a graph plotting the maximum infections of each run"""
    maxinfected_date = find_peak_infections(all_runs)
    for i in maxinfected_date:
        plt.scatter(i[1], i[0])

    plt.show()

def grap_peak_alt(all_runs):
    maxinfected_date = find_peak_infections(all_runs)
    # array of [max infections, date for each max infection]

    maxinfects = 0
    mininfects = maxinfected_date[0][0]
    for i in maxinfected_date:
        if (i[0] > maxinfects):
            maxinfects = i[0] #makes a
        if (i[0] < mininfects):
            mininfects = i[0]

    print("maxinfects = ", maxinfects, " mininfects = ", mininfects)

    xvals = np.arange(0, maxinfects + 1)
    yvals = np.zeros(maxinfects + 1, dtype=int)
    for j in maxinfected_date:
        yvals[j[0]] += 1
        # print(j)

    # print(len(yvals))
    # print(yvals)
    # print(maxinfects / 2)
    # print(type(maxinfects // 2))
    # print(yvals[maxinfects - 100 : maxinfects + 1])

    fig, ax = plt.subplots()
    # ax.bar(xvals[0 : maxinfects + 1], yvals[0: maxinfects + 1], width=1)
    ax.scatter(xvals[0 : maxinfects + 1], yvals[0: maxinfects + 1])
    # ax.set(xlim=(maxinfects - 400, maxinfects + 1))
    ax.set(xlim=(0, maxinfects + 10))

    params, covariates = gaussion_fit(xvals[0 : maxinfects + 1], yvals[0: maxinfects + 1], 7800)

    ax.plot(xvals, gaussian(xvals, params[0], params[1], params[2]), 'r')


    plt.show()

def gaussian(x, A, x_0, sigma):
    y = A * np.exp(-((x - x_0)**2) / (2 * (sigma ** 2)))
    return(y)

def gaussion_fit(x_data, y_data, x_0_guess):

    # guesses
    A = 1
    x_0 = x_0_guess
    sigma = 10
    guess_arr = [A, x_0, sigma]

    params, covs = curve_fit(gaussian, x_data, y_data, guess_arr)

    print(params)
    print(np.sqrt(np.diag(covs)))

    return params, covs


def main():
    """ main function """

    print("running this badboy")

    runs = int(input())

    # print(type(runs))
    # print(runs)

    all_runs = []

    for i in range(runs):
        all_runs.append([])
        data = np.genfromtxt(f'out{i + 1}.txt', dtype=int, delimiter=',', skip_header=1, #skips the header line
            autostrip=False)
        data = np.delete(data, 5, 1) #delete excess column
        all_runs[i] = data

    # print(all_runs[0][:, 2])

    # print(find_peak_infections(all_runs))

    # graph_peak_infections(all_runs)

    grap_peak_alt(all_runs)
    # graph_populations(runs, all_runs)



















if __name__ == '__main__':
    main()
