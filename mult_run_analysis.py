"""

Description: takes data from multiple runs of same parameter values
and plots and analyzes them.
"""

import sys
# import pandas as pd
# from numpy import genfromtxt
import numpy as np




def main():
    """ main function """

    print("running this badboy")

    runs = int(input())

    print(type(runs))
    print(runs)

    all_runs = []

    for i in range(runs):
        # print(type(i))

        # print("i = ", i)
        data = np.genfromtxt(f'out{i + 1}.txt', dtype=int, delimiter=',', skip_header=1, #skips the header line
         autostrip=False)
        all_runs.append(data)

    print(all_runs[0], "\n")
    print(all_runs[runs - 1])


























if __name__ == '__main__':
    main()
