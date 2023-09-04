#problem of the day
"""
Given an array arr[] of N non-negative integers
representing the height of blocks. If width of each
block is 1, compute how much water can be trapped
between the blocks during the rainy season.
Input:  N = 6
        arr[] = { 3, 0, 0, 2, 0, 4}
Output: 10
Explanation:
Bars for input { 3, 0, 0, 2, 0, 4}
Total trapped water = 3 + 3 + 1 + 3 = 10
"""

def trappedWater(arr, n):
    left_max = [0] * n
    right_max = [0] * n
    
    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i])
    
    right_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], arr[i])
    
    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - arr[i]
    
    return trapped_water

# Example input
N = 6
arr = [3, 0, 0, 2, 0, 4]

# Calculate the amount of trapped water
result = trappedWater(arr, N)
print("Amount of trapped water:", result)