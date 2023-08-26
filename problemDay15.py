#problem of the day
"""
Given a string S consisting of
lowercase Latin Letters. Return the first non-repeating character in S.
If there is no non-repeating character return $.
Example 1:
Input: S= hello
Output: h

Explanation: In the given string,the first character which is non-repeatingis h,
as it appears first and there is no other 'h' in the string.
"""
def first_non_repeating_char(S):
    char_count = {}  # Dictionary to store character frequencies
    
    # Count the frequency of each character in the string
    for char in S:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first non-repeating character
    for char in S:
        if char_count[char] == 1:
            return char
    
    return '$'  # Return '$' if no non-repeating character is found

# Example usage
S = "hello"
output = first_non_repeating_char(S)
print(f"first non-repeating character in {S} string is: ",output)  # Output: 'h'
