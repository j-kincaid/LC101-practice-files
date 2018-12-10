# examples

a = 'This is a test just for fun'

join(a.split())
a.replace(' ', '')

# for homework ***********************

def analyze_text(text):
    # Your code here
    """ Count the alphabetical characters; also, the letters 'e'. Return a ratio. """
    total=0
    total_es = 0

    for c in text:
        if c.isalpha():
            total += 1

    total_es = text.lower().count('e')
    percentage = float(total_es/total)

    print(total, total_es, percentage * 100)

## format

def alphabet(text, char):
    for char in (text):
        char = 0
        if char.isalpha() == True:
            char += char
            return char
        
    index = text.find(text)
    if index < 0:
        return text
    num_char = text[:index] + text[index+len(text):]

def find_char(text):
    num_es = False

    for char in text:
        if char == 'e':
            num_es = True
    return num_es
    

def main():
    print(count("Penelope","e"))

if __name__ == "__main__":
    main()

        
num_alphas = 18
num_es = 3

word_news = "I have {0} alphabetical characters" + " and {1} es, a total of {2} characters."
print(word_news.format(num_alphas, num_es, num_alphas + num_es))

word_update = "I still have {alphas} alphabetical characters" + " and {es} es, a percentage of {quotient} characters."
print(word_update.format(alphabetical=num_alphas, es=num_es, quotient=(num_es / num_alphas)))

# print(ord("e")) = 101 so use the accumulator for the e's
# divide the total_char by sum_of_e 
#    num_e = 0
#    for char in (text):
#        if (ord() = 101):
#            num_e += 1
                
#    num_char = str(num_char)
#    num_e = str(num_e)
#    percent = num_e / num_char
#    percent = str(percent)
#    percent = str("num_e" + "percent")
    
#    print("The text contains" + num_char " alphabetic characters, of which " 105 (43.75%)" + " are 'e'.")
          


# Don't copy these tests into Vocareum!
# Note that depending on whether you use str.format or string concatenation
# your code will pass different tests. As long as your code passes either
# tests 1-3 OR tests 4-6, it should pass in Vocareum. See below for more details.
from test import testEqual

# Tests 1-3: solutions using string concatenation should pass these
text1 = "Eeeee"
answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
testEqual(analyze_text(text1), answer1)

text2 = "Blueberries are tasteee!"
answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
testEqual(analyze_text(text2), answer2)

text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
testEqual(analyze_text(text3), answer3)

# Tests 4-6: solutions using str.format should pass these
text4 = "Eeeee"
answer4 = "The text contains 5 alphabetic characters, of which 5 (100%) are 'e'."
testEqual(analyze_text(text4), answer4)

text5 = "Blueberries are tasteee!"
answer5 = "The text contains 21 alphabetic characters, of which 7 (33.33333333333333%) are 'e'."
testEqual(analyze_text(text5), answer5)

text6 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer6 = "The text contains 55 alphabetic characters, of which 0 (0%) are 'e'."
testEqual(analyze_text(text6), answer6)
