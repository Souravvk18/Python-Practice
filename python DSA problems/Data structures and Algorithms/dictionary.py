dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print (dict['Name'])
# print (dict['Age'])

"""
Zara
7
"""
"updating data"

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
# print(dict)

"""
{'Name': 'Zara', 'Age': 8, 'Class': 'First', 'School': 'DPS School'}
"""

"""delete items"""

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# del dict['Name']; # remove entry with key 'Name'
# print(dict)

#{'Age': 8, 'Class': 'First', 'School': 'DPS School'}

# dict.clear(); # remove all entries in dict

"""no duplicate key is allowed. When duplicate keys are encountered during assignment, the last assignment wins."""

dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print ("dict['Name']: ", dict['Name'])

#dict['Name']:  Manni
