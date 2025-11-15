class parent:
  def function(self):
    print("i am good")


class child(parent):
  def _init_(self):
    print("i am bad") 
obj = parent()
pen = child()

pen.function()
output
i am good
