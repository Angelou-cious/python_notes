"""
   Define a property that must have the same value for every class instance (object)

   Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white. Use the following code for this exercise.
"""

class Vehicle:
    """
        A base class for vehicle objects.
    """
    color = "White" # Every Vehicle should be white
    def __init__(self, name, max_speed, mileage):
        """
            Construct a Vehicle object with given name, max speed, and mileage.
        """
        self.name = name # vehicle name
        self.max_speed = max_speed # vehicle max speed
        self.mileage = mileage # vehicle mileage

class Bus(Vehicle):
    """
        A class for bus objects.
    """
    # pass
    def show(self):
        """
            Print the class attribute "color" of Bus object.
            The class attribute "color" is shared by all instances of Bus class.
            The value of "color" is the same for all objects of Bus class.
            The class attribute "color" can be accessed using
                - self.color (from inside the class)
                - Bus.color (from outside the class)
        """
        print(self.color)
class Car(Vehicle):
    """
        A class for car objects.
    """
    pass

bus = Bus('School Volvo', 180, 12)
car = Car('Audi Q5', 240, 18)

print(f'Color: {bus.color}, Vehicle name: {bus.name}, Speed: {bus.max_speed}, Mileage: {bus.mileage}') # print bus properties

print(f'Color: {car.color}, Vehicle name: {car.name}, Speed: {car.max_speed}, Mileage: {car.mileage}') # print car properties

bus.show()
bus2 = Bus.color # This is a class attribute, it is not an instance attribute
print(bus2) # You can access the class attribute "color" using the class name
