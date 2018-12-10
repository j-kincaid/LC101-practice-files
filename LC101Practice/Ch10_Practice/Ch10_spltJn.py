song = "The rain in Spain..."
words = song.split() #split breaks the list into a list of words
print(words)
words = song.split('ai') #ai is a delimiter, it specifies 
# characters to use as word boundaries. 
print(words)
words = ["red" "blue" "green"]
glue = ';' # The separator string, often called the glue
s = glue.join(words) # join the list to form a new string 
print(s)
print(words)

print("***".join(words)) # you can use multi-character strings
print(" ".join(words)) # or empty strings as delimiters. 

xs = list("Crunchy Frog") # And then there's the list conversion function.
print(xs) # It takes each character in the string and places it in a list. 
