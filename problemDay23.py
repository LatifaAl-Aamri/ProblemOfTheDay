#problem of the day 23
"""
Given an array of n integers arr[] where each element represent
the maximum length of jumb that can a made forward from that element.
This means if arr[i]=x , then we can jumpany distance y
such that y <= x . Find the minimum number of jumps to reach the end
of the array ( starting from the first element). If an element is 0, then
you cannot move through that element.
Input: N = 11
       arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3
"""
def minJumps(arr):
    n = len(arr)
    
    # Initialize an array to store the minimum jumps required to reach each position
    jumps = [float('inf')] * n
    jumps[0] = 0  # The minimum jumps required to reach the first position is 0
    
    for i in range(1, n):
        for j in range(i):
            if j + arr[j] >= i:
                # If it's possible to jump from position j to position i
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break  # Once we find a valid jump, we can break out of the inner loop
    
    return jumps[-1]  # The last element contains the minimum jumps required to reach the end

# Example usage
N = 11
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

result = minJumps(arr)
print("Minimum number of jumps:", result)






