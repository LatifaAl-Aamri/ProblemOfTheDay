#problem of day 5
"""
Given a list of N fractions, represented as two lists
numerator and denominator , the task is to determine
the count of pairs of fractions whose sum equals 1.
"""
#ex:
"""
input N=4
numerator = [1,2,2,8]
denominator = [2,4,6,12]
output  2
"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_pairs_with_sum_one(numerator, denominator):
    n = len(numerator)
    count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if numerator[i] * denominator[j] + numerator[j] * denominator[i] == denominator[i] * denominator[j]:
                count += 1
    
    return count

# Example input
N = 4
numerator = [1, 2, 2, 8]
denominator = [2, 4, 6, 12]

result = count_pairs_with_sum_one(numerator, denominator)
print("Output:", result)


























