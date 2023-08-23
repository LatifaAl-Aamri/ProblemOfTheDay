#problem of the day
"""
Given an array A of positive integers , your task is to find
the leader in the array. An element of array is leader
if it is greater than or equal to all the elements to
its right side. The right most element is always a leader.
input: n=6  A[] = {16, 17, 4, 3, 5, 2}
output: 17, 5, 2
"""


#An element in the array is considered a leader if it's
#greater than or equal to all the elements to its right side.
#In other words, it's a leader if no element to its right is greater than it.

def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_right = arr[n - 1]  # The rightmost element is always a leader
    leaders.append(max_right)

    for i in range(n - 2, -1, -1):
        if arr[i] >= max_right:
            max_right = arr[i]
            leaders.append(max_right)

    return leaders[::-1]  # Reverse the list to get the correct order

# Test the function
n = 6
A = [16, 17, 4, 3, 5, 2]
result = find_leaders(A)
print(result)