#FCFS Scheduling
def get_process_input():
    #Function to get process details from user input
    processes = []
    num_processes = int(input("Enter the number of processes: "))
    for i in range(num_processes):
        arrival_time = int(input(f"Enter arrival time for process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        processes.append((i + 1, arrival_time, burst_time))
    return processes

def fcfs_scheduling(processes):
    #Function to perform FCFS scheduling
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # Sorts by arrival time
    
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    total_turnaround_time = 0
    total_waiting_time = 0
    
    #Calculate completion time for each process
    for i in range(n):
        if i == 0:
            completion_time[i] = processes[i][1] + processes[i][2]
        else:
            if processes[i][1] > completion_time[i - 1]:
                completion_time[i] = processes[i][1] + processes[i][2]
            else:
                completion_time[i] = completion_time[i - 1] + processes[i][2]
    
    #Calculate turnaround time and waiting time for each process
    for i in range(n):
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]
        total_turnaround_time += turnaround_time[i]
        total_waiting_time += waiting_time[i]
    
    #Calculates the average turnaround time and waiting time
    avg_turnaround_time = total_turnaround_time / n
    avg_waiting_time = total_waiting_time / n
    
    #Display the results
    print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")
    print(f"\nAverage Turnaround Time: {avg_turnaround_time}")
    print(f"Average Waiting Time: {avg_waiting_time}")

def main():
    try:
        processes = get_process_input()
        fcfs_scheduling(processes)
    except ValueError:
        print("Invalid input. Please enter integer values for times.")

if __name__ == "__main__":
    main()
