
def main():
    job_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arrtime_cpucycle = [[0, 6], [1, 2], [2, 1], [3, 7], [4, 5], [5, 3], [6, 4], [7,5], [8, 7], [9, 2]]

    job_turnaround = []

    FCFS(job_number, arrtime_cpucycle, job_turnaround)

def FCFS(job_number, arrtime_cpucylce, job_turnaround):
    total = 0

    for count in range(len(job_number)):
        sum = 0
        for counter in range(len(job_number) + count - 9):
            sum += arrtime_cpucylce[counter][1]
        
        job_turnaround.append(sum)

    for count in range(len(job_turnaround)):
        job_turnaround[count] = job_turnaround[count] - arrtime_cpucylce[count][0]
        total += job_turnaround[count]

    print("Average Turnaround Time: {0}".format(total / len(job_number)))


main()