#______________THE SLICE OPERATOR

cats = "Honey, Safa, and Feather"
print(cats[0:5])
print(cats[7:11])
print(cats[17:25])

# The slice operator [n:m] measures from the nth character to 
# the mth, including the first but excluding the last. 
# Start with index n and go up to index m - 1. 

cat = "Clementine"
print(cat[:2]) # If you put the colon first the slice stats at the 
# beginning of the string. 
print(cat[2:]) # If you put the colon at the end, the slice 
# goes to the end of the string. 
print(cat[:]) # This is not a slice. 