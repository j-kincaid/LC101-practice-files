# Dictionaries are mutable so you can change their 
# contents like lists. 

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
	
del inventory['pears']

print(inventory)

inventory['bananas'] = inventory['bananas'] + 200

print(inventory)