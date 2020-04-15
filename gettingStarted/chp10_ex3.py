try:
    print(5/0)
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Program keeps going on!")

try:
    open('someNoneExistingFile', 'r')
except FileNotFoundError:
    # print('File not found!')
    pass

print("Program keeps going on without any notifications!")
