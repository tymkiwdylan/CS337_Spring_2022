# Dylan Tymkiw
# CS337
# Project 2
# 02/16/2022


from numpy import empty
import process

# First Come First Serve Scheduler


def FCFS_scheduler(processes, ready, CPU, time, quantum, verbose=True):

    # pick process with lowest arrival time and remove it from ready

    process = ready.pop(find_arrival_time(ready))

    # set start time to time
    start_time = time

    # while process is not finished
    while process.duty[0] != 0:

        # decrement process burst time by one
        process.duty[0] -= 1

        # add 1 to time
        time += 1

        # add processes that arrived now to ready queue
        add_ready(processes, ready, time)

        for i in range(len(ready)):
            ready[i].wait_time += 1

    # set end time to time
    end_time = time

    if verbose:
        print(f"Process: {process.get_ID()} Start: {start_time}  End:{end_time}")

    # add processID, start, end to CPU (this will be useful later)
    CPU.append(
        dict(
            process=process.get_ID(),
            Start=start_time,
            Finish=end_time,
            Priority=process.get_priority(),
            wait_time=process.get_wait_time(),
            Turnaround_time=(end_time - start_time) + process.get_wait_time(),
        )
    )

    return time


# Priority Scheduler
def priority_scheduler(processes, ready, CPU, time, quantum, verbose=True):
    # pick process with lowest burst time and remove it from ready
    process = ready.pop(find_max_priority(ready))

    # set start time to time
    start_time = time

    # while process is not finished
    while process.duty[0] != 0:

        # decrement process burst time by one
        process.duty[0] -= 1

        # add 1 to time
        time += 1

        # add processes that arrived now to ready queue
        add_ready(processes, ready, time)
        # updates wait time
        for i in range(len(ready)):
            ready[i].wait_time += 1

    # set end time to time
    end_time = time
    if verbose:
        print(f"Process: {process.get_ID()}  Start: {start_time}  End:{end_time}")

    # add processID, start, end to CPU (this will be useful later)
    CPU.append(
        dict(
            process=process.get_ID(),
            Start=start_time,
            Finish=end_time,
            Priority=process.get_priority(),
            wait_time=process.get_wait_time(),
            Turnaround_time=(end_time - start_time) + process.get_wait_time(),
        )
    )

    return time


# Shortest Job First Scheduler
def SJF_scheduler(processes, ready, CPU, time, quantum, verbose=True):
    # pick process with lowest burst time and remove it from ready

    process = ready.pop(find_shortest_job(ready))

    # set start time to time
    start_time = time

    # while process is not finished
    while process.duty[0] != 0:

        # decrement process burst time by one
        process.duty[0] -= 1

        # add 1 to time
        time += 1

        # add processes that arrived now to ready queue
        add_ready(processes, ready, time)

        for i in range(len(ready)):
            ready[i].wait_time += 1

    # set end time to time
    end_time = time
    if verbose:
        print(f"Process: {process.get_ID()}  Start: {start_time}  End:{end_time}")

    # add processID, start, end to CPU (this will be useful later)
    CPU.append(
        dict(
            process=process.get_ID(),
            Start=start_time,
            Finish=end_time,
            Priority=process.get_priority(),
            wait_time=process.get_wait_time(),
            Turnaround_time=(end_time - start_time) + process.get_wait_time(),
        )
    )

    return time


def round_robin(processes, ready, CPU, time, quantum=2, verbose=True):

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
        time += 1

        # add processes that arrived now to ready queue
        add_ready(processes, ready, time)

        update_wait_time(ready)

    update_arrival(process, time, ready)

    # set end time to time
    end_time = time

    if verbose:
        print(f"Process: {process.get_ID()}  Start: {start_time}  End:{end_time}")

    # add processID, start, end to CPU (this will be useful later)
    CPU.append(
        dict(
            process=process.get_ID(),
            Start=start_time,
            Finish=end_time,
            Priority=process.get_priority(),
            wait_time=process.get_wait_time(),
            Turnaround_time=(end_time - start_time) + process.get_wait_time(),
            Response_time=start_time - process.get_arrival_time(),
        )
    )

    return time


def SRT_scheduler(processes, ready, CPU, time, quantum, verbose=True):
    # pick process with lowest burst time and remove it from ready

    process = ready.pop(find_SRT(ready))

    # set start time to time
    start_time = time

    # while process is not finished
    while process.duty[0] != 0:

        # decrement process burst time by one
        process.duty[0] -= 1

        # add 1 to time
        time += 1

        # add processes that arrived now to ready queue
        add_ready(processes, ready, time)

        update_wait_time(ready)

        if is_shorter(ready, process.get_duty()[0]):
            break

    update_arrival(process, time, ready)

    # set end time to time
    end_time = time
    if verbose:
        print(f"Process: {process.get_ID()}  Start: {start_time}  End:{end_time}")

    # add processID, start, end to CPU (this will be useful later)
    CPU.append(
        dict(
            process=process.get_ID(),
            Start=start_time,
            Finish=end_time,
            Priority=process.get_priority(),
            wait_time=process.get_wait_time(),
            Turnaround_time=(end_time - start_time) + process.get_wait_time(),
            Response_time=start_time - process.get_arrival_time(),
        )
    )

    return time


def PP_scheduler(
    processes, ready, CPU, time, quantum, verbose=True
):  # Review this for when preemptive starts
    # pick process with lowest burst time and remove it from ready
    process = ready.pop(find_max_priority(ready))

    # set start time to time
    start_time = time

    # while process is not finished
    while process.duty[0] != 0 and not (find_max(ready, process.get_priority())):

        # decrement process burst time by one
        process.duty[0] -= 1

        # add 1 to time
        time += 1

        # add processes that arrived now to ready queue
        add_ready(processes, ready, time)

        update_wait_time(ready)

    update_arrival(process, time, ready)

    # set end time to time
    end_time = time
    if verbose:
        print(f"Process: {process.get_ID()}  Start: {start_time}  End:{end_time}")

    # add processID, start, end to CPU (this will be useful later)
    CPU.append(
        dict(
            process=process.get_ID(),
            Start=start_time,
            Finish=end_time,
            Priority=process.get_priority(),
            wait_time=process.get_wait_time(),
            Turnaround_time=(end_time - start_time) + process.get_wait_time(),
            Response_time=start_time - process.get_arrival_time(),
        )
    )

    return time


def completely_fair_scheduler(processes, ready, CPU, time, target_latency = 5, verbose = True):

    start_time = time
    process = ready.remove_min_vruntime()

    if ready.size != 0:
        dynamic_quantum = (int) (target_latency/ready.size)
        if dynamic_quantum < 1:
            dynamic_quantum = 1
    else:
        dynamic_quantum = 1
    
    time += dynamic_quantum

    process.duty[0] -= dynamic_quantum


    for i in range(len(processes)):
        if processes[i].get_arrival_time() == time:
            ready.insert(processes[i].vruntime, processes[i])
            print(f'process: {processes[i].get_ID()} added')

    end_time = time

    process.set_vruntime((end_time - start_time)*process.weight)
    
    if process.duty[0] != 0:
        ready.insert(process.vruntime, process)
        print(f'process: {process.get_ID()} re added with vruntime of {process.vruntime}')

    

    if verbose:
        print(f"Process: {process.get_ID()}  Start: {start_time}  End:{end_time}")

    CPU.append(
        dict(
            process=process.get_ID(),
            Start=start_time,
            Finish=end_time,
            Priority=process.get_priority(),
            wait_time=process.get_wait_time(),
            Turnaround_time=(end_time - start_time) + process.get_wait_time(),
            Response_time=start_time - process.get_arrival_time(),
        )
    )

    return time



# Helper Function for finding the shortest job
def find_shortest_job(ready):
    process = 0
    min = ready[0].get_duty()[0]
    for i in range(len(ready)):
        if ready[i].get_duty()[0] < min:
            min = ready[i].get_duty()[0]
            process = i
    return process


# Helper function for finding max priority process
def find_max_priority(ready):

    max = ready[0].get_priority()
    process = 0
    for i in range(len(ready)):
        if ready[i].get_priority() > max:
            max = ready[i].get_priority()
            process = i

    return process


def find_SRT(ready):
    process = 0
    min = ready[0].duty[0]
    for i in range(len(ready)):
        if ready[i].duty[0] < min:
            min = ready[i].duty[0]
            process = i
    return i


# Helper function for finding the arrival time
def find_arrival_time(ready):

    process = 0
    min = ready[0].get_arrival_time()
    for i in range(len(ready)):
        if ready[i].get_arrival_time() < min:
            process = i
    return process


# Helper function for adding processes to the ready queue.
def add_ready(processes, ready, time):
    for i in range(len(processes)):
        if processes[i].get_arrival_time() == time:
            ready.append(processes[i])


def find_max(ready, max):
    if not ready:
        return False
    else:
        for item in ready:
            if item.get_priority() > max:
                return True

    return False


def update_arrival(process, time, ready):
    if process.duty[0] != 0:
        process.set_arrival_time(time)
        ready.append(process)


def update_wait_time(ready):
    for i in range(len(ready)):
        ready[i].wait_time += 1


def is_shorter(ready, job_time):
    if not ready:
        return False
    else:
        for item in ready:
            if item.get_duty()[0] < job_time:
                return True
            else:
                return False
