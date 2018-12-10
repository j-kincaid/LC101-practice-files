#def is_letter(string, char):

#    for i in range(len(text)):
#        i = ""
#        if (data[i].isalpha() == True):
#            i+=i
#        return int(i)
#        if (i == 'e') == True:
#            nums_e = ""
#            i = text.count('e')
#        return int(i)
#        i = nums_e


def alphabet(text, char):
    for char in (text):
        char = ''
        if char.isalpha() == True:
            char += char
            return char
        return False

def main():
    print(alphabet("compsci", 'e'))
    print(alphabet("aAbEefIijOopUus", 'e'))

if __name__ == "__main__":
    main()
