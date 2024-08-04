#N meetings in one room
class Solution:
    
    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        # Create a list of tuples where each tuple contains (start_time, end_time)
        meetings = list(zip(start, end))
        
        # Sort the meetings based on the end time
        meetings.sort(key=lambda x: x[1])
        
        # Initialize count of meetings and set the end time of the last meeting selected
        count = 1
        last_end_time = meetings[0][1]
        
        # Iterate through the sorted list of meetings
        for i in range(1, n):
            # If the current meeting starts after the last selected meeting ends, select it
            if meetings[i][0] > last_end_time:
                count += 1
                last_end_time = meetings[i][1]
        
        # Return the count of maximum meetings that can be accommodated
        return count

# Example usage:
solution = Solution()

n1 = 6
start1 = [1, 3, 0, 5, 8, 5]
end1 = [2, 4, 6, 7, 9, 9]
print(solution.maximumMeetings(n1, start1, end1))  # Output: 4

n2 = 3
start2 = [10, 12, 20]
end2 = [20, 25, 30]
print(solution.maximumMeetings(n2, start2, end2))  # Output: 1
