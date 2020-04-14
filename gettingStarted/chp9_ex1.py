class Dog:
    """A Simple atemp to make a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " is now rolling over.")


my_dog = Dog('miskoş', '3.5')
my_cat = Dog('misiklet', '3.5')

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

my_cat.sit()
my_cat.roll_over()

