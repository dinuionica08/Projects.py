# python is an object oriented programming language
#almost everything in pythons is an objects with proprieties and methods

# a class example with an constructor and a function
class Person:
  def __init__(self, name, age, passions):
    self.name = name
    self.age = age
    self.passions = passions

  def informations(self):
      print("This persone is " , self.name)
      print("This persone is " , self.age, " years old ")
      print("This persone is passionate about  " , self.passions)

p1 = Person("John", 36,["footbla","music"])

print(p1.name)
print(p1.age)
p1.informations()