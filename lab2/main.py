class Process:
    def __init__(self, name, burst_time):
        self.name = name
        self.burst_time = burst_time
        self.remaining_time = burst_time

def round_robin(processes, time_quantum):
    n = len(processes)
    queue = []
    time_elapsed = 0

    while True:
        all_processes_completed = True

        for process in processes:
            if process.remaining_time > 0:
                all_processes_completed = False

                if process.remaining_time <= time_quantum:
                    time_elapsed += process.remaining_time
                    process.remaining_time = 0
                    print(f"{process.name} completed")

                else:
                    time_elapsed += time_quantum
                    process.remaining_time -= time_quantum
                    print(f"{process.name} executed for {time_quantum} units")

                queue.append(process)

        if all_processes_completed:
            break

    print("\nRound Robin Scheduling Result:")
    print(f"Total Time Elapsed: {time_elapsed}")

# Example usage
if __name__ == "__main__":
    processes = [
        Process("P1", 10),
        Process("P2", 5),
        Process("P3", 8),
    ]

    time_quantum = 2
    round_robin(processes, time_quantum)
