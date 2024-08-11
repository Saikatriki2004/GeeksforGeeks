class Solution:
    
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        
        # Step 1: Sort jobs by descending order of profit
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
        # Step 2: Find the maximum deadline to determine the size of the timeline
        max_deadline = max(job.deadline for job in Jobs)
        
        # Step 3: Initialize a timeline to keep track of available slots
        timeline = [-1] * (max_deadline + 1)  # Index 0 is ignored
        
        total_profit = 0
        job_count = 0
        
        # Step 4: Iterate over sorted jobs and try to schedule them
        for job in Jobs:
            # Find a free slot for this job (from its deadline to the start)
            for slot in range(job.deadline, 0, -1):
                if timeline[slot] == -1:  # If the slot is free
                    timeline[slot] = job.id
                    total_profit += job.profit
                    job_count += 1
                    break
        
        return job_count, total_profit

# To represent the Job structure, you can use a class or namedtuple.
# For example:

class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

# Example usage:
jobs = [Job(1, 4, 20), Job(2, 1, 1), Job(3, 1, 40), Job(4, 1, 30)]
n = len(jobs)

sol = Solution()
print(sol.JobScheduling(jobs, n))  # Output: (2, 60)
