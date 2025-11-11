# Sum of First N Natural Numbers Write a Python program using a while loop to find the sum of first n natural numbers.
# Sum of First N Natural Numbers
n = int(input("Enter a positive integer (n): "))
if n < 0:
    print("Please enter a positive integer.")
else:
    total_sum = 0
    counter = 1
    while counter <= n:
        total_sum += counter
        counter += 1
    print(f"The sum of the first {n} natural numbers is: {total_sum}")
output
Enter a positive integer (n): 3
The sum of the first 3 natural numbers is: 6
