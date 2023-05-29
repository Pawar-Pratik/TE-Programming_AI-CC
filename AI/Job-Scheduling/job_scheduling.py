def schedule_jobs(jobs):
    # Sort the jobs in decreasing order of their profits
    sorted_jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    # Create an empty schedule
    schedule = []

    # Initialize the time slot array
    time_slots = [-1] * len(jobs)

    # Fill the schedule by assigning jobs to time slots
    for i in range(len(sorted_jobs)):
        # Find the next available time slot
        for j in range(sorted_jobs[i][1] - 1, -1, -1):
            if time_slots[j] == -1:
                time_slots[j] = sorted_jobs[i][0]
                schedule.append(sorted_jobs[i])
                break

    return schedule


# Take job information as user input
num_jobs = int(input("Enter the number of jobs: "))
jobs = []
for i in range(num_jobs):
    job_id = i + 1
    deadline = int(input(f"Enter the deadline for job {job_id}: "))
    profit = int(input(f"Enter the profit for job {job_id}: "))
    jobs.append((job_id, deadline, profit))

result = schedule_jobs(jobs)
print("Job schedule:")
for job in result:
    print(f"Job {job[0]} (Deadline: {job[1]}, Profit: {job[2]})")
