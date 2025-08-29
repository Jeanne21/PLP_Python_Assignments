# Base class
class Animal:
    def move(self):
        print("This animal moves in some way.")

# Subclasses overriding move() (Polymorphism)
class Dog(Animal):
    def move(self):
        print("The dog runs")

class Fish(Animal):
    def move(self):
        print("The fish swims")

class Bird(Animal):
    def move(self):
        print("The bird flies")

# Create objects
animals = [Dog(), Fish(), Bird()]

# Polymorphism in action
for animal in animals:
    animal.move()
