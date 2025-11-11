# Largest of Three Numbers Write a Python program to find the largest among three numbers.
num1 = int(input("enter the num1:"))
num2 = int(input("enter the num2:"))
num3 = int(input("enter the num3:"))
if (num1>num2)&(num1>num3):
    largest = num1
elif (num2>num1)&(num2>num3):
    largest = num2
else:
    largest = num3
print("the largest number is",largest)
out put
enter the num1:99
enter the num2:110
enter the num3:199
the largest number is 199

[ ]
