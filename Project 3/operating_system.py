# Dylan Tymkiw
# CS337
# Project 1
# 02/16/2022

import pandas as pd
import process
import scheduler
import numpy as np
import RBTree

# This function runs the selected scheduler until the ready que is empty


def kernel(selected_scheduler, processes, quantum, file_name, verbose=True):
    CPU = []
    ready = RBTree.RBTree()
    time = 0

    for i in range(len(processes)):
        if processes[i].get_arrival_time() == time:
            ready.insert(processes[i].vruntime, processes[i])
    

    while ready.size != 0:
        time = selected_scheduler(processes, ready, CPU, time, verbose=verbose)

    # save results as CSV
    df = pd.DataFrame(CPU)
    df.to_csv(file_name, index=False)

    cal_data = df.to_numpy()

    avg_turnaround = np.average(cal_data[:, -2])
    avg_wait = np.average(cal_data[:, -3])
    avg_response = np.mean(cal_data[:-1])
    return avg_turnaround, avg_wait, avg_response


# I moved the testing code to Jupyter Notebook.
