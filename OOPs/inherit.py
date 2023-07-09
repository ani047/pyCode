# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

# Child Class (inherits from Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class's constructor
        self.breed = breed

    def speak(self):
        print("Dog barks")

    def fetch(self):
        print("Dog fetches the ball")

# Create instances of the classes
animal = Animal("Generic Animal")
dog = Dog("Buddy", "Labrador")

# Accessing parent class method
animal.speak()  # Output: Animal speaks

# Accessing child class method
dog.speak()  # Output: Dog barks

# Accessing inherited method from parent class
dog.fetch()  # Output: Dog fetches the ball

# Accessing inherited property from parent class
print(dog.name)  # Output: Buddy
print(dog.speak())