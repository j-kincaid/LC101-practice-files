from test import testEqual

def analyze_text(text, char):

    len_of_string = len(text)
    data = str(text)
  
    for char in range(len_of_string):
        if (data[char].isalpha() == False):
            return False
    return True
    data[char]= (data[char] + 1)
    return data[char]
        num_es = 0
        if text[char] == 'e':
            num_es = num_es + num_es
    return num_es






