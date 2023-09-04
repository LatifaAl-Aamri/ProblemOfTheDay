#problem of the day
"""
Given a non-negative integer N .
The task is to check if N is power of 2. More formally, check if N can
be expressed as 2^x for same integer x :
input: N = 8
Output:  yes
"""
def is_power_of_2(n):
    # Check if n is greater than 0 and its binary representation has a single '1' bit
    return n > 0 and (n & (n - 1)) == 0

# Input
N = int(input("Enter a non-negative integer: "))

# Check if N is a power of 2
if is_power_of_2(N):
    print("Output: yes")
else:
    print("Output: no")
