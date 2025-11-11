# Even/Odd and Positive/Negative Combined Write a Python program that checks whether a number is:
num = int(input("Enter an integer:"))
if num % 2 == 0: 
    if num > 0:
        print(f"The number {num} is Even and Positive.")
    elif num < 0:
        print(f"The number {num} is Even and Negative.")
    else:
        print(f"The number {num} is Even and Zero.")
else: 
    if num > 0:
        print(f"The number {num} is Odd and Positive.")
    elif num < 0:
        print(f"The number {num} is Odd and Negative.")
    else:
        print(f"The number {num} is Odd and Zero.") 
out put
Enter an integer: 28
The number 28 is Even and Positive.
