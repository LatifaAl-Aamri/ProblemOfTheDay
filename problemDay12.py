#problem of the day
"""
Given an unsorted array Arr of N positive and negative numbers,
your task is to create an array of alternate positive and negative
numbers without changing the relative order of positive and
negative numbers.
input: N = 9
       Arr{} = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:  9, -2, 4, -1, 5, -5, 0, -3, -2
"""

def alternate_positive_negative(arr):
    positives = [x for x in arr if x >= 0]
    negatives = [x for x in arr if x < 0]

    result = []
    pos_index = 0
    neg_index = 0

    for num in arr:
        if num >= 0:
            result.append(positives[pos_index])
            pos_index += 1
        else:
            result.append(negatives[neg_index])
            neg_index += 1

    return result

# Example input
N = 9
Arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]

output = alternate_positive_negative(Arr)
print(', '.join(map(str, output)))
