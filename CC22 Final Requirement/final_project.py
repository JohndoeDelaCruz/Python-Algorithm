class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)
    
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.start_time = current_time
        process.completion_time = process.start_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        current_time += process.burst_time

def print_processes(processes):
    print("PID\tArrival\tBurst\tStart\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.start_time}\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")

# Sample data
process_list = [
    Process(1, 0, 4),
    Process(2, 1, 3),
    Process(3, 2, 1),
    Process(4, 3, 2)
]





# Runs the scheduling
fcfs_scheduling(process_list)

# Print processes
print_processes(process_list)