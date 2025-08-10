


# Define a class named Vehicle
class Vehicle:
    # constructor method to initialize object's state
    def __init__(self, max_speed, mile):
        # instance attributes
        self.max_speed = max_speed # maximum speed
        self.mile = mile # mileage

    # instance method to show the max speed
    def show(self):
        # print max speed
        print(f'max speed: {self.max_speed}')

    # instance method to show the mileage
    def mileage(self):
        # print mileage
        print(f'mile: {self.mile}')

# create an object of Vehicle class
car = Vehicle(10, 10)

# print the max speed and mileage of the car
print(car.mile, car.max_speed)

# call the show method to show the max speed
car.show()

# call the mileage method to show the mileage
car.mileage()
