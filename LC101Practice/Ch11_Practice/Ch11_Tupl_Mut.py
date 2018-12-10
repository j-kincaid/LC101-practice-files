juliet = ("Juliet", "Kincaid", "913-548-2856", "jkwryter@gmail.com") # A tuple is 
# a sequence of items of any type. Tuples are immutable.
# If we try to use item assignment as in 
# juliet[0] we get an error. 
# To change it you have to slice it and concatenate to 
# make a new tuple.
print(juliet[2:3])
print(len(juliet))
print(juliet)

# Tuples can return tuples as return values. 
def circle_info(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return (c, a)

print(circle_info(10))



# The tuple ASSIGNMENT FEATURE allows a tuple of variable on
# the left to be assigned values from a tuple on the right. 
# juliet = ('Juliet', 'Kincaid', '913-548-2856', 'jkwryter@gmail.com')
(name, surname, phone, email) = juliet

# The number of values on the left must match the number
# of elements in the tuple. 
# The left side is a tuple of variables, the 
# right side is a tuple of values.