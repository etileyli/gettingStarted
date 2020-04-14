class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to define a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("Increment value should be non-negative.")

class ElectricCar(Car):
    """Represents aspects of a car specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initializes the attributes of parent class."""
        super().__init__(make, model, year)


my_new_car = Car('Renault', 'Clio', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(47)
my_new_car.read_odometer()
my_new_car.update_odometer(46)
my_new_car.read_odometer()
my_new_car.increment_odometer(50)
my_new_car.read_odometer()
my_new_car.increment_odometer(-25)
my_new_car.read_odometer()

print()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())