#problem of the day
"""
Given an array arr[] containing positive elements.
A and B are two numbers defining a range. The task is to check
if the array contains all elements in the given range.
Input: N=7, A=2, B=5
       arr[]={1,4,5,2,7,8,3}
Output: yes
explanation: It has elements between range 2-5 , i.e: 2,3,4,5
"""

def check_elements_in_range(arr, A, B):
    # Create a set to keep track of elements in the range
    range_set = set(range(A, B + 1))
    
    # Iterate through the array
    for num in arr:
        # If an element is in the range set, remove it
        if num in range_set:
            range_set.remove(num)
        
        # If all elements in the range are found, return True
        if not range_set:
            return True
    
    # If any element in the range is missing, return False
    return False

# Example input
N = 7
A = 2
B = 5
arr = [1, 4, 5, 2, 7, 8, 3]

# Check if all elements in the range are present
if check_elements_in_range(arr, A, B):
    print("Output: yes")
else:
    print("Output: no")
