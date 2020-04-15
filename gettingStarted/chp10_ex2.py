file_name = 'programming.txt'

with open(file_name, 'a') as file_object:
    file_object.write('Hello World!\n')

"""Python can only write strings to a text fie. If you want to store numerical data in a
text fie, you’ll have to convert the data to string format fist using the str() function."""