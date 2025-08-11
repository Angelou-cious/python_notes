"""
    OOP Exercise 7: Check type of an object

    Write a program to determine which class a given Bus object belongs to.
    
    This script defines a Vehicle class and a Bus class that inherits from Vehicle.
    It then creates an instance of Bus and checks its type using the type() function.
"""

class Vehicle:  # Define the Vehicle class as a blueprint for vehicle objects
    def __init__(self, name, mileage, capacity):  # Constructor method to initialize Vehicle instances
        self.name = name  # Assign the name parameter to the instance's name attribute
        self.mileage = mileage  # Assign the mileage parameter to the instance's mileage attribute
        self.capacity = capacity  # Assign the capacity parameter to the instance's capacity attribute

class Bus(Vehicle):  # Define the Bus class that inherits from Vehicle
    pass  # Use pass to indicate that the class has no additional methods or attributes beyond those inherited from Vehicle

School_bus = Bus("School Volvo", 12, 50)  # Create an instance of Bus with specific name, mileage, and capacity values

print(type(School_bus))  # Print the type of the School_bus instance to determine its class