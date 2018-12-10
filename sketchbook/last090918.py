def analyze_text(text):
    # Your code here
    """ Count the alphabetical characters; also, the letters 'e'. Return a ratio. """
    data = str(text)
    
# To Do: Find alphabetical characters

    for char in text:
        nums_alpha = ''
        if data[char].isalpha() == True:
            nums_alpha = nums_alpha + data[char]
    return nums_alpha
# To Do: Find letters 'e'
        nums_e = False
        if char == 'e':
            nums_e = True
            nums_e += nums_e
    return nums_e

# To Do: Divide letters 'e' by alphabeticals
    nums_e = int(nums_e)
    nums_alpha = int(nums_alpha)
    q = nums_e/ nums_alpha
    quotient = float(q * 100)

# Return analysis in text
    return ("The text contains " + nums_alpha + " alphabetic characters, of which " + nums_e + " (" + quotient + "%) are 'e'.")

