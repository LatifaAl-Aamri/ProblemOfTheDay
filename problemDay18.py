#Problem of the day
"""
There one meeting room in a firm .
There are N meetings in the form of (start[i], end[i]) where start[i] is
start time of meeting i and end[i] is finish time of meeting i.
what is the maximum number of meetings that can be accommodated
in the meeting room when only one meeting can be help
in the meeting room at a particular time?
Note: Start time of one chosen meeting can't be equal
to the end time of the other chosen meeting.
Input:  N = 6
        start[] = {1, 3, 0, 5, 8, 5}
        end[] = {2, 4, 6, 7, 9, 9}
Output: 4
Explanation: maximum 4 meetings can be help with given
start and timings the meetings are (1,2), (3,4), (5,7), (8,9)
"""

def maximumMeetings(N, start, end):
    # Create a list of meetings with their start and end times
    meetings = [(start[i], end[i], i) for i in range(N)]
    
    # Sort the meetings by their end times in ascending order
    meetings.sort(key=lambda x: x[1])
    
    # Initialize variables to keep track of the maximum meetings and the end time of the last scheduled meeting
    max_meetings = 0
    last_end_time = -1
    
    # Iterate through the sorted meetings
    for meeting in meetings:
        start_time, end_time, index = meeting
        
        # If the current meeting's start time is greater than or equal to the end time of the last scheduled meeting, schedule it
        if start_time >= last_end_time:
            max_meetings += 1
            last_end_time = end_time
    
    return max_meetings

# Example input
N = 6
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

# Find the maximum number of meetings that can be accommodated
result = maximumMeetings(N, start, end)
print("Maximum number of meetings:", result)







