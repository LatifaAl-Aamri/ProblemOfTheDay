"""
user should enter array of numbers and you are giving the number,
one of the two numbers that equals the sum of the giving number.
ex: input--> num=[1,2,3,5,6]   t=9
    output--> 5,4
          --> 3,6
"""

def find_pairs_with_sum(nums, target):
    pairs = []
    seen = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs

# Get input from the user
nums = list(map(int, input("Enter an array of numbers: ").split()))
target = int(input("Enter the target sum: "))

# Find pairs with the target sum
pairs = find_pairs_with_sum(nums, target)

# Display the pairs
if pairs:
    for pair in pairs:
        print(f"{pair[0]}, {pair[1]}")
else:
    print("No pairs found with the target sum.")

