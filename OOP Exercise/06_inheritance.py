
"""
    Class Inheritance

    Create a Bus child class that inherits from the Vehicle class. The default fare charge for any vehicle is its seating capacity multiplied by 100 (seating capacity * 100).

    If the vehicle is a Bus instance, we need to add an extra 10% to the full fare as a maintenance charge. Therefore, the total fare for a Bus instance will be the final amount, calculated as total fare plus 10% of the total fare. (final amount = total fare + 10% of the total fare.)

    Note: The bus seating capacity is 50, so the final fare amount should be 5500.

    Use the following code for your parent Vehicle class. We need to access the parent class from within a method of a child class.
"""

class Vehicle:
    def __init__(self, name, mileage, capacity):
        # initialize the Vehicle object with a name, mileage and capacity
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        # calculate the total fare based on the capacity
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        # calculate the total fare for Bus type
        total_fare = super().fare()
        # add an extra 10% to the total fare for maintenance
        final_amount = total_fare + (total_fare * .10)
        return final_amount

# create a Bus object
School_bus = Bus("School Volvo", 12, 50)
# print the total fare for the Bus
print(f"Total Bus fare is: , {School_bus.fare():.2f}")
