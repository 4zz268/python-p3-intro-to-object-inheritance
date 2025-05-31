# Example: Inheritance, Composition, and Decorators in Python

# Superclass (Parent)
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound."

# Subclass (Child) using inheritance and super()
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        return f"{self.name} barks!"
    def info(self):
        return f"{self.name} is a {self.breed}."

# Composition example
class Collar:
    def __init__(self, color):
        self.color = color
    def describe(self):
        return f"Collar color: {self.color}"

class PetDog(Dog):
    def __init__(self, name, breed, collar_color):
        super().__init__(name, breed)
        self.collar = Collar(collar_color)  # Composition: PetDog has a Collar
    def show_collar(self):
        return self.collar.describe()

# Decorator example
def excited(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper

class Parrot(Animal):
    @excited
    def speak(self):
        return f"{self.name} says hello"

# Usage examples
if __name__ == "__main__":
    dog = PetDog("Buddy", "Golden Retriever", "red")
    print(dog.speak())           # Inherited and overridden method
    print(dog.info())            # Unique to Dog
    print(dog.show_collar())     # Composition

    parrot = Parrot("Polly")
    print(parrot.speak())        # Decorated method
