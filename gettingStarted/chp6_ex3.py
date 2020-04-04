# Create an empty list
aliens = []

for alien_number in range (30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

print('Total number of aliens created: ' + str(len(aliens)))

'''
for alien_number in range(0, 30, 2):
    for value in aliens[alien_number]:
        aliens[alien_number][value] = 'red'

i = 0
for alien in aliens:
    print('alien number ' + str(i) + ' is ' + alien['color'])
    i = i + 1
print('...')
'''

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10

for alien in aliens:
    print(alien)
