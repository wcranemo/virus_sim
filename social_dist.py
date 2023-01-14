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


def plot_runs(run_data_arr, var_len_arr):

    healthy_clr = "b"
    infected_clr = "r"
    recovered_clr = "g"
    dead_clr = "k"

    # fig = plt.figure()
    # fig, axs = plt.subplots(var_len_arr[0], var_len_arr[1]) #sharex=True, sharey=True)
    x = run_data_arr[0][0][0]["time"]

    # print(run_data_arr[0][0][0])

    # print(run_data_arr[0][0][0].info())
    # print(run_data_arr[0][0][0][0]#['healthy_population'])
    # )
    print(run_data_arr[0][0][0])
    print(run_data_arr[0][0][0].columns.tolist())

    testfig, testax = plt.subplots()

    for i in range(len(x)):
        print(x[i], run_data_arr[0][0][0]["healthy_population"][i])
    testax.plot(x, run_data_arr[0][0][0]["healthy_population"], healthy_clr)
    testax.plot(x, run_data_arr[0][0][0]["infected_population"], infected_clr, label="Infected")
    testax.plot(x, run_data_arr[0][0][0]["recovered_population"], recovered_clr, label="Recovered")
    testax.plot(x, run_data_arr[0][0][0]["dead_population"], dead_clr, label="Dead")

    # put label in graph (done here so legend is only printed once)
    # axs[0,0].plot(0, run_data_arr[0][0][0]['healthy_population'][0], healthy_clr, label="Healthy")
    # axs[0,0].plot(0, run_data_arr[0][0][0]["infected_population"][0], infected_clr, label="Infected")
    # axs[0,0].plot(0, run_data_arr[0][0][0]["recovered_population"][0], recovered_clr, label="Recovered")
    # axs[0,0].plot(0, run_data_arr[0][0][0]["dead_population"][0], dead_clr, label="Dead")


    # for k in range(var_len_arr[0]):
    #     for j in range(var_len_arr[1]):
    #         for i in range(var_len_arr[2]):
    #             axs[k, j].plot(x, run_data_arr[k][j][i]["healthy_population"], healthy_clr) #, label="Healthy"
                # axs[k, j].plot(x, run_data_arr[k][j][i]["infected_population"], infected_clr) #, label="Infected"
                # axs[k, j].plot(x, run_data_arr[k][j][i]["recovered_population"], recovered_clr) #, label="Recovered"
                # axs[k, j].plot(x, run_data_arr[k][j][i]["dead_population"], dead_clr) #, label="Dead"

    # axs.set_ylabel("# of People")
    # axs.set_xlabel("Days")

    # axs.legend()
    plt.show()


def plot_alt(data_arr, ind_dict):

    healthy_clr = "b"
    infected_clr = "r"
    recovered_clr = "g"
    dead_clr = "k"

    fig, axs = plt.subplots(data_arr.shape[0], data_arr.shape[1], sharex='all', sharey='all')

    xs = data_arr[0][0][0][:, 0]

    # axs.plot(data_arr[1][1][0][:, ind_dict["Healthy"]], healthy_clr)
    # axs.plot(data_arr[1][1][0][:, ind_dict["Infected"]], infected_clr)
    # axs.plot(data_arr[1][1][0][:, ind_dict["Recovered"]], recovered_clr)
    # axs.plot(data_arr[1][1][0][:, ind_dict["Dead"]], dead_clr)

    # print("data arr shape is ", data_arr.shape)

    for k in range(data_arr.shape[0]):
        for j in range(data_arr.shape[1]):
            for i in range(data_arr.shape[2]):
                axs[k,j].plot(data_arr[k][j][i][:, ind_dict["Healthy"]], healthy_clr)
                axs[k,j].plot(data_arr[k][j][i][:, ind_dict["Infected"]], infected_clr)
                axs[k,j].plot(data_arr[k][j][i][:, ind_dict["Recovered"]], recovered_clr)
                axs[k,j].plot(data_arr[k][j][i][:, ind_dict["Dead"]], dead_clr)

    plt.show()

def main():

    inp_strs = input().split()
    runs_per_param = int(inp_strs[0])
    runtime = int(inp_strs[1])

    print("\nruns_per_param = ", runs_per_param)
    print("runtime = ", runtime)

    param_df = pd.read_csv('params.txt')

    run_data_arr = []
    len_soc_dist = int(param_df.shape[0] / param_df.shape[1])
    len_conn_red = param_df.shape[1]

    # var_len_arr = [len_conn_red, len_soc_dist, runs_per_param]
    # for k in range(len_conn_red):
    #     run_data_arr.append([])
    #     for j in range(len_soc_dist):
    #         run_data_arr[k].append([])
    #         for i in range(runs_per_param):
    #             # i += 1
    #             # print(i)
    #             run_data_arr[k][j].append([])
    #             df = pd.read_csv('out_{0}_{1}_{2}.txt'.format(k + 1, j + 1, i + 1))
    #             run_data_arr[k][j][i] = df

    # print(len(run_data_arr), len(run_data_arr[0]), len(run_data_arr[0][0]))

    # for i in range(runs):
    #     all_runs.append([])
    #     data = np.genfromtxt(f'out{i + 1}.txt', dtype=int, delimiter=',', skip_header=1, #skips the header line
    #         autostrip=False)
    #     data = np.delete(data, 5, 1) #delete excess column
    #     all_runs[i] = dat

    # plot_runs(run_data_arr, var_len_arr)

    num_metrics = 5 #number of columns in csv

    data_arr = np.empty([len_conn_red, len_soc_dist, runs_per_param, runtime, num_metrics])

    # df = pd.read_csv('out_1_1_1.txt')
    # # print(df)
    # print(df.columns.tolist())
    # df.drop(df.columns[5], axis=1)
    # # df.drop('Unnamed: 5', axis=1)
    # print(df.columns.tolist())
    # numpy = df.to_numpy()
    # print(numpy)

    ind_dict = {"Healthy" : 1, "Infected" : 2, "Recovered" : 3, "Dead" : 4}

    for k in range(len_conn_red):
        for j in range(len_soc_dist):
            for i in range(runs_per_param):
                # df = pd.read_csv('out_{0}_{1}_{2}.txt'.format(k + 1, j + 1, i + 1))
                # data_arr[k][j][i] = df.to_numpy()

                data = np.genfromtxt('out_{0}_{1}_{2}.txt'.format(k + 1, j + 1, i + 1),
                dtype=int, delimiter=',', skip_header=1, autostrip=False)
                data = np.delete(data, 5, 1) #delete excess column
                data_arr[k][j][i] = data


    # print(data_arr[0][0][0][:, 1][:15])

    plot_alt(data_arr, ind_dict)














if __name__ == '__main__':
    main()
