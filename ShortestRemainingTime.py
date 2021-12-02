
def main():
    job_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    job_arrival = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    job_cpu = [6, 2, 1, 7, 5, 3, 4, 5, 7, 2]

    SRT(job_no, job_arrival, job_cpu)

def SRT(job_no, job_arrival, job_cpu):
    temp_no = job_no.copy()
    temp_arrival = job_arrival.copy()
    temp_cpu = job_cpu.copy()
    job_queue, cpu_queue = [], []
    turnaround, job_order = [], []
    total = 0

    totalSum = sum(temp_cpu)

    count, indicator, flag, lowest = 0, 0, 0, 999

    while count < totalSum:
        counter = 0
        lowest = 999

        if indicator < len(job_no):
            for counter in range(indicator, len(temp_arrival)):
                if temp_arrival[counter] <= count:
                    job_queue.append(temp_no[indicator])
                    cpu_queue.append(temp_cpu[temp_no.index(temp_no[indicator])])
                    indicator += 1

        counter = 0
        for counter in range(len(cpu_queue)):
            if lowest > cpu_queue[counter]:
                lowest = cpu_queue[counter]
                flag = cpu_queue.index(lowest)

        count += 1
        cpu_queue[flag] = cpu_queue[flag] - 1

        if cpu_queue[flag] == 0:
            turnaround.append(count)
            job_order.append(temp_arrival[job_no.index(job_queue[flag])])
            del job_queue[flag]
            del cpu_queue[flag]

    count = 0
    for count in range(len(turnaround)):
        turnaround[count] = turnaround[count] - job_order[count]
        total += turnaround[count]

    count = 0

    print("TURNAROUND TIME")
    for count in range(len(job_no)):
        counter = 0
        for counter in range(len(job_no)):
            if count == job_order[counter]:
                print("JOB {0}: {1}".format(count+1, turnaround[counter]))

    print("Average Turnaround Time: {0}".format(total / len(job_no)))

main()