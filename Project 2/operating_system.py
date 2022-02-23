# Dylan Tymkiw
# CS337
# Project 1
# 02/16/2022

import pandas as pd
import process
import scheduler
import numpy as np

# This function runs the selected scheduler until the ready que is empty


def kernel(selected_scheduler, processes, quantum, verbose=True):  # Remember to add calculation for Average TT and WT
    CPU = []
    ready = []
    time = 0

    for i in range(len(processes)):
        if processes[i].get_arrival_time() == time:
            ready.append(processes[i])

    while ready:
        time = selected_scheduler(processes, ready, CPU, time, quantum=quantum, verbose=verbose)

    # save results as CSV
    df = pd.DataFrame(CPU)
    df.to_csv(str(selected_scheduler), index=False)

    cal_data = df.to_numpy()

    avg_turnaround = np.average(cal_data[:, -1])
    avg_wait = np.average(cal_data[:, -2])
    return avg_turnaround, avg_wait


# I moved the testing code to Jupyter Notebook.

