#problem of the day
"""
Given a string S .The task is to count the number of substring
which contains equal number of lowercase and uppercase letters.
input: S = "WomensDAY"
output: There are 4 substring of given string which satisfy the condition.
They are "Wo" "ensDAY" "nsDA" and "sD".
"""

def count_equal_case_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub_str = s[i:j]
            lower_count = sum(1 for char in sub_str if char.islower())
            upper_count = sum(1 for char in sub_str if char.isupper())
            
            if lower_count == upper_count:
                substrings.append(sub_str)
    
    return substrings

# Example usage
S = "WomensDAY"
result = count_equal_case_substrings(S)
print("There are", len(result), "substrings of the given string that satisfy the condition.")
print("They are", result)





