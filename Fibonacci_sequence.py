n = int(input("enter the number"))
a, b = 0,1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b
 out put
enter the number7
0 1 1 2 3 5 8 
