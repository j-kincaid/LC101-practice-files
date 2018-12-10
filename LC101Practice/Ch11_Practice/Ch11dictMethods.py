inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
# The keys method returns a view of its underlying keys
for akey in inventory.keys():     # The keys method: the 
    # order in which we get the keys is not defined
   print("Got key", akey, "which maps to value", inventory[akey])

key_list = list(inventory.keys()) # We can turn the view
# into a list with the list conversion function. 
print(key_list)

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory:
   print("Got key", k)  # You can even omit the keys method 
   # call in the for loop. 

print(list(inventory.values())) # values and items methods 
# are similar to keys.
print(list(inventory.items()))

for (k,v) in inventory.items():
    # The items are shown as tuples containing the key and 
    # associated value.
    print("Got", k, "that maps to", v)

for k in inventory:
    print("Got", k, "that maps to", inventory[k])

# in and not in can test for the presence of a key in a 
# dictionary

print('apples' in inventory)
print('cherries' in inventory)
if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")


# The get method allows you to enter a second parameter.
print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries", 0))

######### The statement iterates over the keys by lengths 
# of string.
total = 0
my_dict = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
if len(akey) > 3:
    total = total + my_dict[akey]
print(total)
