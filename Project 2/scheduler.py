#Dylan Tymkiw
#CS337
#Project 2
#02/16/2022

import queue
import re

from numpy import empty
import process

#First Come First Serve Scheduler
def FCFS_scheduler(processes, ready, CPU, time, quantum, verbose = True):


     
 
     # pick process with lowest arrival time and remove it from ready
    
    process = ready.pop(find_arrival_time(ready))
            

 
    # set start time to time
    start_time = time
    

    # while process is not finished
    while not (process.get_burst_time() == 0):
 
        # decrement process burst time by one
        process.burst_time -= 1
       
        # add 1 to time
        time +=1
 
        # add processes that arrived now to ready queue
        add_ready(processes, ready, time)

        for i in range(len(ready)):
            ready[i].wait_time += 1
        

 
    # set end time to time
    end_time = time

    if verbose:
        print(f'Process: {process.get_ID()}  Start: {start_time}  End:{end_time}')
 
    # add processID, start, end to CPU (this will be useful later)
    CPU.append(dict(process=process.get_ID(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    wait_time = process.get_wait_time(),
                    Turnaround_time = (end_time - start_time)+ process.get_wait_time()))
 
    return time
  
  
#Helper function for finding the arrival time
def find_arrival_time(ready): #Make sure to revisit this. You need to delete the item AFTER you pick the process

    process = 0
    min = ready[0].get_arrival_time()
    for i in range(len(ready)):
        if ready[i].get_arrival_time() < min:
            process = i
    return process
    
#Helper function for adding processes to the ready queue.
def add_ready(processes, ready, time):
    for i in range(len(processes)):
        if processes[i].get_arrival_time() == time:
            ready.append(processes[i])

#Priority Scheduler
def priority_scheduler(processes, ready, CPU, time, verbose = True):
    # pick process with lowest burst time and remove it from ready
    process = ready.pop(find_max_priority(ready))

    # set start time to time
    start_time = time

    # while process is not finished
    while not (process.get_burst_time() == 0):
 
        # decrement process burst time by one
        process.burst_time -= 1
       
        # add 1 to time
        time +=1
 
        # add processes that arrived now to ready queue
        add_ready(processes, ready, time)
        #updates wait time
        for i in range(len(ready)):
            ready[i].wait_time += 1
        

 
    # set end time to time
    end_time = time
    if verbose:
        print(f'Process: {process.get_ID()}  Start: {start_time}  End:{end_time}')
 
    # add processID, start, end to CPU (this will be useful later)
    CPU.append(dict(process=process.get_ID(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    wait_time = process.get_wait_time(),
                    Turnaround_time = (end_time - start_time)+ process.get_wait_time()))
 
    return time

#Shortest Job First Scheduler
def SJF_scheduler(processes, ready, CPU, time, verbose = True):
    # pick process with lowest burst time and remove it from ready
    
    process = ready.pop(find_shortest_job(ready))

 
    # set start time to time
    start_time = time


    # while process is not finished
    while not (process.get_burst_time() == 0):
 
        # decrement process burst time by one
        process.burst_time -= 1
       
        # add 1 to time
        time +=1
 
        # add processes that arrived now to ready queue
        add_ready(processes, ready, time)

        for i in range(len(ready)):
            ready[i].wait_time += 1
        

 
    # set end time to time
    end_time = time
    if verbose:
        print(f'Process: {process.get_ID()}  Start: {start_time}  End:{end_time}')
 
    # add processID, start, end to CPU (this will be useful later)
    CPU.append(dict(process=process.get_ID(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    wait_time = process.get_wait_time(),
                    Turnaround_time = (end_time - start_time)+ process.get_wait_time()))
 
    return time

#Helper Function for finding the shortest job
def find_shortest_job(ready):
    process = 0
    min = ready[0].get_burst_time()
    for i in range(len(ready)):
        if ready[i].get_burst_time() < min:
            process = i
    return i

#Helper function for finding max priority process
def find_max_priority(ready):

    max = ready[0].get_priority()
    process = 0
    for i in range(len(ready)):
        if ready[i].get_priority() > max:
            process = i
    return process



def round_robin(processes, ready, CPU, time, quantum, verbose = True):
    
    # pick process with lowest arrival time and remove it from ready
    
    process = ready.pop(find_arrival_time(ready))
            

 
    # set start time to time
    start_time = time

    aux_quantum = quantum
    

    # while process is not finished
    while (aux_quantum != 0) and (process.duty[0] != 0):
 
        # decrement process duty[0] time by one
        process.duty[0] -= 1
        aux_quantum -= 1
       
        # add 1 to time
        time +=1
 
        # add processes that arrived now to ready queue
        add_ready(processes, ready, time)

        update_wait_time(ready)
        
    update_arrival(process, time, ready)
 
    # set end time to time
    end_time = time

    if verbose:
        print(f'Process: {process.get_ID()}  Start: {start_time}  End:{end_time}')
 
    # add processID, start, end to CPU (this will be useful later)
    CPU.append(dict(process=process.get_ID(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    wait_time = process.get_wait_time(),
                    Turnaround_time = (end_time - start_time)+ process.get_wait_time()))
 
    return time


def update_arrival(process, time, ready):
    if process.duty[0] != 0:
        process.set_arrival_time(time)
        ready.append(process)

def update_wait_time(ready):
    for i in range(len(ready)):
            ready[i].wait_time += 1


def SRT_scheduler(processes, ready, CPU, time, quantum, verbose = True):
    # pick process with lowest burst time and remove it from ready
    
    process = ready.pop(find_SRT(ready))

 
    # set start time to time
    start_time = time

    aux_quantum = quantum

    # while process is not finished
    while aux_quantum != 0 and process.duty[0] != 0 :
 
        # decrement process burst time by one
        process.duty[0] -= 1
        aux_quantum -= 1
       
        # add 1 to time
        time +=1
 
        # add processes that arrived now to ready queue
        add_ready(processes, ready, time)

        update_wait_time(ready)
        
    update_arrival(process, time, ready)
 
    # set end time to time
    end_time = time
    if verbose:
        print(f'Process: {process.get_ID()}  Start: {start_time}  End:{end_time}')
 
    # add processID, start, end to CPU (this will be useful later)
    CPU.append(dict(process=process.get_ID(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    wait_time = process.get_wait_time(),
                    Turnaround_time = (end_time - start_time)+ process.get_wait_time()))
 
    return time


def find_SRT(ready):
    process = 0
    min = ready[0].duty[0]
    for i in range(len(ready)):
        if ready[i].duty[0] < min:
            process = i
    return i

def PP_scheduler(processes, ready, CPU, time,quantum, verbose = True): #Review this for when preemptive starts
    # pick process with lowest burst time and remove it from ready
    process = ready.pop(find_max_priority(ready))

    # set start time to time
    start_time = time


    # while process is not finished
    while process.duty[0] != 0:
 
        # decrement process burst time by one
        process.duty[0] -= 1
       
        # add 1 to time
        time +=1
 
        # add processes that arrived now to ready queue
        add_ready(processes, ready, time)

        update_wait_time(ready)

        if find_max(ready, process.get_priority()): #Something is going on with priority
            break
        
    update_arrival(process, time, ready)
        

 
    # set end time to time
    end_time = time
    if verbose:
        print(f'Process: {process.get_ID()}  Start: {start_time}  End:{end_time}')
 
    # add processID, start, end to CPU (this will be useful later)
    CPU.append(dict(process=process.get_ID(),
                    Start=start_time,
                    Finish=end_time,
                    Priority=process.get_priority(),
                    wait_time = process.get_wait_time(),
                    Turnaround_time = (end_time - start_time)+ process.get_wait_time()))
 
    return time


def find_max(ready, max):
    if not ready:
        return False
    else:
        for item in ready:
            if item.get_priority() > max:
                return True
            else:
                return False