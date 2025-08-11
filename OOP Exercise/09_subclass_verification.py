
"""
    Check object is a subclass of a particular class
    
    This script demonstrates class inheritance relationships by defining an animal hierarchy
    and using issubclass() to verify subclass relationships between different classes.
"""

class Animal:  # Base class for all animals
    pass  # Animal class has no attributes or methods defined yet

class Dog(Animal):  # Dog class inherits from Animal
    pass  # Dog class has no additional attributes or methods beyond Animal

class Puppy(Dog):  # Puppy class inherits from Dog (which itself inherits from Animal)
    pass  # Puppy class has no additional attributes or methods beyond Dog

class Cat:  # Cat class is independent and does not inherit from Animal
    pass  # Cat class has no attributes or methods defined

print(issubclass(Dog, Animal))  # True: Dog is a subclass of Animal
print(issubclass(Animal, Dog))  # False: Animal is not a subclass of Dog
print(issubclass(Cat, Animal))  # False: Cat is not a subclass of Animal
print(issubclass(Puppy, Animal))  # True: Puppy inherits from Dog which inherits from Animal