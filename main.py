#MULTIPLE INHERITANCE
class Classmate:

  def __init__(self, name, cls):
    self.name = name
    self.cls = cls

  def show(self):
    print(f"My friend name is {self.name}. He reads in {self.cls}")


class AreaFriend:

  def __init__(self, name, area):
    self.name = name
    self.area = area

  def show(self):
    print(f"My friend name is {self.name}. He lives in {self.area}")


class Friend(Classmate, AreaFriend):  #MULTIPLE INHERITANCE

  def __init__(self, name, cls, area):
    self.name = name
    self.cls = cls
    self.area = area


f1 = Friend("Masum", "", "Shalbagan")
f1.show()  #first a classmate dewa ache, ejonno classmate class call hobe
f2 = Friend("Mahmud", "4th Year", "")
f2.show()
a = AreaFriend("Masum", "Shalbagan")
a.show()
