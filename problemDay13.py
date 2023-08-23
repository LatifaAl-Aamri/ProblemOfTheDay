#problem of the day
"""
Given a set of integers, find add distinct sums
that can be generated from the subsets of the
given sets.
Input: nums = {1, 2}
Output:  {0, 1, 2, 3}
"""
def find_distinct_sums(nums):
    distinct_sums = set()
    distinct_sums.add(0)  # Include the empty subset sum

    for num in nums:
        new_sums = set()
        for summation in distinct_sums:
            new_sum = num + summation
            new_sums.add(new_sum)
        distinct_sums |= new_sums  # Union of the current distinct_sums and new_sums

    return sorted(list(distinct_sums))

# Example input
nums = {1, 2}
output = find_distinct_sums(nums)
print(output)
