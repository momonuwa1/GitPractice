class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print('Bark')


class Cat(Mammal):
    pass

dog1 = Dog()
dog1.bark()

