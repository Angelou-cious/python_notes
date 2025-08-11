"""
    Determine if School_bus is also an instance of the Vehicle class
    
    This script demonstrates inheritance in OOP by creating a Bus class that inherits from Vehicle,
    then checking if a Bus instance is also considered an instance of the Vehicle class.
"""


class Vehicle:  # Define the base Vehicle class for all vehicle types
    def __init__(self, name, mileage, capacity):  # Constructor to initialize Vehicle attributes
        self.name = name  # Set the vehicle's name attribute
        self.mileage = mileage  # Set the vehicle's mileage attribute
        self.capacity = capacity  # Set the vehicle's passenger capacity attribute

class Bus(Vehicle):  # Define Bus class that inherits all properties and methods from Vehicle
    pass  # No additional attributes/methods - inherits everything from Vehicle

School_bus = Bus("School Volvo", 12, 50)  # Create a Bus instance with specific attributes

print(isinstance(School_bus, Vehicle))  # Check if Bus instance is also considered a Vehicle instance
