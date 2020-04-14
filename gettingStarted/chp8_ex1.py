def greet_user():
    """Display a simple greeting!"""
    print("Hello!")


greet_user()


# def describe_pet(animal_type= 'cat', pet_name= 'misiklet'):
    # """Display information about pet."""
    # print("\nI have a " + animal_type + ".")
    # print("My " + animal_type + "'s name is " + pet_name.title() + ".")

def describe_pet(animal_type, pet_name= 'misiklet'):
    """Display information about pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type='kedi', pet_name='miskos')
# describe_pet(pet_name='miskos')
describe_pet(animal_type='cat')

