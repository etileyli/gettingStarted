responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in a dictionary
    responses[name] = response

    repeat = input("Would you like to let another person to respond? (yes/no) ")
    if (repeat == "no"):
        polling_active = False

# Polling is complete. Show the results
print('\n---Polling Results---')
for name, response in responses.items():
    print(name + " would like to climb to mountain " + response + ".")
