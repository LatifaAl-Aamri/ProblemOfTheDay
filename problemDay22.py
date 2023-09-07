#problem of the day 22
"""
Given two sorted arrays of distinct elements.
There is only 1 difference between the arrays.
First array has one element extra added in between.
find the index of extra element.
Input:  N = 7
        A[] = {2, 4, 6, 8, 9, 10, 12}
        B[] = {2, 4, 6, 8, 10, 12}
Output: 4
"""
def findExtraElementIndex(arr1, arr2):
    n = len(arr2)
    index = n  # Initialize index to the last position

    # Iterate through both arrays
    for i in range(n):
        if arr1[i] != arr2[i]:
            index = i
            break  # Stop when the first difference is found

    return index

# Example usage
N = 7
A = [2, 4, 6, 8, 9, 10, 12]
B = [2, 4, 6, 8, 10, 12]

result = findExtraElementIndex(A, B)
print("Index of extra element:", result)