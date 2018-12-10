def analyze_text(text):
    # Your code here
    """ Count the alphabetical characters; also, the letters 'e'. Return a ratio. """
    len_of_string = len(text)
    data = str(text)
    
# To Do: Find alphabetical characters

nums_alpha = ''

for index in range(length_of_string):
    if data[index].isalpha() == True:
        nums_alpha = nums_alpha + data[index]
return nums_alpha
#    nums_alpha = int(nums_alpha)


# To Do: Find letters 'e'

nums_e = False

for char in data:
    if char == 'e':
        nums_e = True
return nums_e

# To Do: Divide letters 'e' by alphabeticals

q = int(nums_e) / int(nums_alpha)
quotient = float(q * 100)

# Return analysis in text


word_news = "I have {0} alphabetical characters" + " and {1} es, a total of {2} characters."
print(word_news.format(nums_alpha, nums_e, nums_alpha + nums_e))

word_update = "I still have {alphas} alphabetical characters" + " and {es} es, a percentage of {quotient} characters."
print(word_update.format(alphabetical=nums_alpha, es=nums_e, quotient=(nums_e / nums_alpha)))

