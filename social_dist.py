"""
compares runs of different parameter values, specifically different cutoffs for
when social distancing is enacted, as well as how much daily interactions are
reduced when it is enacted
"""

import sys
import pandas as pd
# from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt


def plot_runs(run_data_arr):

    healthy_clr = "b"
    infected_clr = "r"
    recovered_clr = "g"
    dead_clr = "k"

    fig, ax = plt.subplots(len(run_data_arr), len(run_data_arr[0]))

    # for k in len(run_data_arr):
    #     for j in run
    # put label in graph
    axs.plot(0, run_data_arr[0][0]["healthy_population"][0], healthy_clr, label="Healthy")
    ax.plot(0, run_data_arr[0][0]["infected_population"][0], infected_clr, label="Infected")
    ax.plot(0, run_data_arr[0][0]["recovered_population"][0], recovered_clr, label="Recovered")
    ax.plot(0, run_data_arr[0][0]["dead_population"][0], dead_clr, label="Dead")

    for k in range(len(run_data_arr)):
        for j in range(len(run_data_arr[0])):
            for i in :
                # y.append([])
                # y[i] = all_runs[i][:, 1] #living population
                ax.plot(x, all_runs[i][:, 1], healthy_clr) #, label="Healthy"
                ax.plot(x, all_runs[i][:, 2], infected_clr) #, label="Infected"
                ax.plot(x, all_runs[i][:, 3], recovered_clr) #, label="Recovered"
                ax.plot(x, all_runs[i][:, 4], dead_clr) #, label="Dead"

    ax.set_ylabel("# of People")
    ax.set_xlabel("Days")

    ax.legend()
    plt.show()




def main():

    runs_per_param = int(input())
    print("runs_per_param = ", runs_per_param)

    # soc_dist_params = int(input())
    # conn_red_params = int(input())
    # print(con)

    param_df = pd.read_csv('params.txt')
    # print(param_df)
    # print(param_df.shape)
    # print(len(param_df))
    # print('\n')

    run_data_arr = []
    len_soc_dist = int(param_df.shape[0] / param_df.shape[1])
    len_conn_red = param_df.shape[1]

    var_len_arr = [len_conn_red, len_soc_dist, runs_per_param]
    for k in range(len_conn_red):
        run_data_arr.append([])
        for j in range(len_soc_dist):
            run_data_arr[k].append([])
            for i in range(runs_per_param):
                # i += 1
                # print(i)
                run_data_arr[k][j].append([])
                df = pd.read_csv('out_{0}_{1}_{2}.txt'.format(k + 1, j + 1, i + 1))
                run_data_arr[k][j][i] = df

    print(len(run_data_arr), len(run_data_arr[0]), len(run_data_arr[0][0]))

    # for i in range(runs):
    #     all_runs.append([])
    #     data = np.genfromtxt(f'out{i + 1}.txt', dtype=int, delimiter=',', skip_header=1, #skips the header line
    #         autostrip=False)
    #     data = np.delete(data, 5, 1) #delete excess column
    #     all_runs[i] = dat



















if __name__ == '__main__':
    main()
