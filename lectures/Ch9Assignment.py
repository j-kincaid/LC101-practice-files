### This one passed ###

def analyze_text(text):
    data = str(text)

    length = len(text)
    print("The length is", length)
    length_alpha = 0
    count_for_eE = 0
    for i in range(0, length):
        if(data[i].isalpha()):
            length_alpha = length_alpha + 1
            if (data[i] == 'e' or data[i] == 'E'):
                count_for_eE = (count_for_eE + 1)


    percentage = ((count_for_eE / length_alpha) * 100)
    answer = ("The text contains "+ str(length_alpha)+ " alphabetic characters, of which " + str(count_for_eE)+ " (" + str(percentage)+"%) are 'e'.")
    return answer

text = "ceguwdlxabJCDglCHioxhwqEEeeg"
analyze_text(text)