# Aliasing can occur with dictonaries
# So here's a dictionary:
foods = {'cucumber': 'vegetable', 'apple': 'fruit', 'bread': 'starch'}
# foods is a dictionary that contains pairs of foods and 
# food groups

alias = foods

print(alias is foods)

alias['apple'] = 'vegetable'
print(foods['cucumber'])

# Ok now copy. You can modify the dictionary and keep a copy 
# of the original with the copy method. It's like cloning a 
# dictionary object. 

acopy = foods.copy()
acopy['bread'] = 'starch' # does not change foods

my_dict = {"cat":12, "dog":6, "elephant":23, "bear":20}
your_dict = my_dict
your_dict["elephant"] = 999
print(my_dict["elephant"]) # your_dict is an alias for 
# my_dict, and so the value for the key elephant has 
# been changed.

