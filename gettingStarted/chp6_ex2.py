favorite_languages = {
    'emre': 'c',
    'ebru': 'python',
    'gizem': 'csharp',
    'birisi': 'python',
}

print(favorite_languages)

for key, value in favorite_languages.items():
    print('\nPerson: ' + key)
    print('Favorite language: ' + value)

i = 0
for key in favorite_languages.keys():
    i = i + 1
    print('\nKey ' + str(i) + ': ' + key)

i = 0
for key in sorted(favorite_languages):
    i = i + 1
    print('\nKey ' + str(i) + ': ' + key)

i = 0
for values in set(favorite_languages.values()):
    i = i + 1
    print('\nValue ' + str(i) + ': ' + values)
