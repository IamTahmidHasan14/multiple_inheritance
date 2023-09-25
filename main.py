#SINGLE INHERITANCE
class Animal:

  def __init__(self, name, type):
    self.name = name
    self.type = type

  def sound(self):
    print(f"Sound by a {self.type}")


class Cat(Animal):

  def __init__(self, name, chield):
    super().__init__(name, type="cat")
    self.chield = chield

  def sound(self):
    print("Meaw!")


c = Cat("Lusni", "Mini")
c.sound()
a = Animal("Lusni", "Cat")
a.sound()
