#___________________STRING METHODS

# Strings are objects and they have their own methods. 
# Some methods are ord and chr. 
# Two more:

ss = "Hello, Kitty"
print(ss + "  Original string")

ss = ss.upper()
print(ss + " .upper")

tt = ss.lower()
print(tt + " .lower")

cap = ss.capitalize() # Capitalizes the first character only. 
print(cap + " .capitalize")

strp = ss.strip() # Returns a string with the 
print(strp + " .strip")  ## leading and trailing whitespace removed. 

lstrp = ss.lstrip()
print(lstrp + " .lstrip")  # Returns a string with the leading
# whitespace removed. 

rstrp = ss.rstrip()
print(rstrp + " .rstrip")  # Returns a string with the trailing
# whitespace removed. 

cout = ss.count("T") # Returns number of occurrences of a character
print(cout)

news = ss.replace("T", "^") # replaces all occurrences of an old substring 
print(news) # with a new one.