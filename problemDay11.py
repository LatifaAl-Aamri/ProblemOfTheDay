#problem of the day
"""
Given a string S, find the longest palindromic substring
in S . Substring of string S:S[i....j] where 0 <= i <= j < len (S)
Palindrome string A string that reads the same backward.
More formally S is palindrome if reverse (S) = S
In case of conflict return the substring which occurs first
(with the leust starting index)
Input: aaabbaa
Output: aabbaa
Explanation: The longest palindromic substring is "aabbaa"
"""

def longest_palindromic_substring(s):
    n = len(s)
    # Initialize a 2D array to store palindrome information
    dp = [[False] * n for _ in range(n)]

    start = 0  # Start index of the longest palindrome
    max_length = 1  # Length of the longest palindrome

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for substrings of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # Check if the current substring is a palindrome
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length

    return s[start:start + max_length]

# Test the function
input_str = "aaabbaa"
output = longest_palindromic_substring(input_str)
print(output)  # Output: "aabbaa"
