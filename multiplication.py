# Multiplication Table Write a Python program to print the multiplication table of any number entered by the user using a for loop.
num = int(input("Enter a number to see its multiplication table: "))
print(f"Multiplication Table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}") 
out put
Enter a number to see its multiplication table:  2
Multiplication Table for 2:
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
