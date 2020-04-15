file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    contents = file_object.read()
    print(contents)

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

some_number = str(16)
if some_number in pi_string:
    print("it's in!!")
else:
    print("Unfortunately not in!")