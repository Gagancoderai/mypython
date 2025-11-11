# Grade CalculationWrite a Python program to input marks and display the grade as per the following rule Marks ≥ 90 → Grade A Marks ≥ 75 → Grade B  Marks ≥ 50 → Grade C Else → Fail
mark = int(input("enter the mark"))
if mark>=90:
    print("Grade A")
elif mark>=70:
    print("Grade B")
elif mark>=50:
    print("Grade C")
else:
    print("fail")
out put
enter the mark 85
Grade B
