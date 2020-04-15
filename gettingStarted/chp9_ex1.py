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

    def fill_gas_tank(self):
        """Some conventional car specific function"""


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement that describes the battery size"""
        print("This car has a " + str(self.battery_size) + "-kwH battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """Represents aspects of a car specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initializes the attributes of parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tank"""
        print("Electric cars don't have gas tank.")


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
# my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
