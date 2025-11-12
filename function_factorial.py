# Write a function factorial() that finds the factorial of a given number using a loop.
def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers"
    elif number == 0:
        return 1
    else:
        fact = 1
        for i in range(1, number + 1):
            fact *= i
        return fact
# Example usage:
num = 5
print(f"The factorial of {num} is: {factorial(num)}")
 Out put
 The factorial of 5 is: 120
 
