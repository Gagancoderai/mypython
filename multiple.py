class A:
  def fun1(self):
    print("day 01")
class B:
  def fun02(self):
    print("day 02")
class C(A,B):
  pass
obj = A()
obj2 = B()
obj.fun1()
obj2.fun02() 
out put 
day 01
day 02
