"""
    Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
"""


class Vehicle:  # Base class Vehicle
    def __init__(self, name, max_speed, mileage):  # Initialize Vehicle with name, max_speed, and mileage
        self.name = name  # Assign name
        self.max_speed = max_speed  # Assign max_speed
        self.mileage = mileage  # Assign mileage

    def seating_capacity(self, capacity):  # Method to return seating capacity
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    

class Bus(Vehicle):  # Bus class inherits from Vehicle

    def seating_capacity(self, capacity=50):  # Override seating_capacity with default capacity of 50
        return super().seating_capacity(capacity=capacity)  # Call the parent class method with default capacity


bus = Bus('School Volvo', 180, 12)  # Create an instance of Bus with name, max_speed, and mileage

print(bus.seating_capacity())  # Print the seating capacity of the bus with default value
