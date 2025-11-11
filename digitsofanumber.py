# Count Digits of a Number
num = int(input("Enter an integer: "))

if num == 0:
    print("The number 0 has 1 digit.")
else:
    count = 0
    # Handle negative numbers by taking absolute value
    temp_num = abs(num)
    while temp_num > 0:
        temp_num = temp_num // 10  # Integer division to remove the last digit
        count += 1
    print(f"The number {num} has {count} digits.")
out put
Enter an integer: 2
The number 2 has 1 digits.
