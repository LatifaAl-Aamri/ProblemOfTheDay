"""
Write a program that comparing three numbers
and get the largest number
(user should enter the numbers)
"""


def get_largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        
        largest_number = get_largest_number(num1, num2, num3)
        print(f"The largest number is: {largest_number}")
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


main()





"""

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

if (num1 > num2 & num1 > num3):
    print(f"the first number is the largest number, {num1}")
elif (num2 > num1 & num2 > num3):
    print(f"the second number is the largest number, {num2}")
elif (num3 > num1 & num3 > num2):
    print(f"the third number is the largest number, {num3}")
else:
    print("all numbers are equals")
    
"""