class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

p1 = Person("Tom", 15)
p1.name = "David"
print(p1.name)