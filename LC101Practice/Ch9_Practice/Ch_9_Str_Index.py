##_________________THE INDEXING OPERATOR 
# selects a single character from a string, accessing each
# by its index value. 

# Positive positions are indexed from left to right. 
# Negative positions, right to left. 

cat = "Clementine"
a_character = cat[5] # Creates a new string with just one character. 
print(a_character)

first_char = cat[0]
print(first_char)

last_char = cat[-1]

print(last_char)

##_________________ INDEXING A STRING 

# Use the len function

cat = "Honey" 
print(len(cat))

# Find the last character with the index value:

last = cat[len(cat)-1]
print(last)

