bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[3].title() + "."
print(message)
bicycles.append('sth')
message = "My first bicycle was a " + bicycles[4].title() + "."
print(message)
bicycles.insert(0, 'new bicycle')
print(bicycles)
del bicycles[0]
print(bicycles)
print('')
bicycles.sort()
print(bicycles)
bicycles.sort(reverse=True)
print(bicycles)
print(sorted(bicycles))

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.reverse()
print(bicycles)
print(bicycles[-1])

for bicycle in bicycles:
    print(bicycle)