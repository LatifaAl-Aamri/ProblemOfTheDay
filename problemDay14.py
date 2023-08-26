# problem of the day
"""
Given string s representing a postfix expression,
the task is to evaluate the expression and find the final value
operators will only include the basic arithmetic operators
like *, /, + and -
Input: s = "231*+9-"
Output: -4
Explanation: After solving the given expression,
we have -4 as result.
"""
def evaluate_postfix_expression(s):
    stack = []

    for char in s:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)  # Assuming division results in float

    return stack[0]

s = "231*+9-"
result = evaluate_postfix_expression(s)
print(result)
"""
In this code, we iterate through the characters of the input string.
If the character is a digit, we convert it to an integer and push it onto the stack.
If it's an operator, we pop the top two elements from the stack, apply the operator,
and push the result back onto the stack.
Finally, the top element of the stack will contain the final result of the postfix expression.
"""






