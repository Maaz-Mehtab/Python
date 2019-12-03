# Queston 1: Use a dictionary to store information about a person you know. Store their first name, last name, age,
# and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print
# each piece of information stored in your dictionary. Add a new key value pair about qualification then
# update the qualification value to high academic level then delete it.
person = {
    'first_name': 'Maaz',
    'last_name': 'Mehtab',
    'age': 24,
    'city': 'Karachi',
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
dict = {'Name': 'Maaz', 'Age.': 24, 'City': 'Karachi','Qualification': 'BESE'}
print("dict['Name']: ", dict['Name'])
print("dict['Age.']: ", dict['Age.'])
print("dict['City']: ", dict['City'])
print("dict['Qualification']: ", dict['Qualification'])
dict = {'Name': 'Maaz', 'Age.': 24, 'city': 'Karachi', 'Qualification.': 'BESE'}
print("The Qualification:", dict.get('Qualification'))
dict['Qualification'] = 'MSC'
print("The Qualification replaced: [Update]", dict.get('Qualification'))
dict['Qualification'] = 'MSC'
print("The Qualification: [Addition]", dict.get('Qualification'))
num_dict = {1: 'MAaz', 2: 'BESE'}
# Delete all elements from the dictionary
num_dict.clear()
print(num_dict)