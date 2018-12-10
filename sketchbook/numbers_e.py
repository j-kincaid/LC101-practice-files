def find_char(text):
    nums_e = False

    for char in text:
        if char == 'e':
            nums_e = True
    return nums_e

def main():
    print(find_char("compsci"))
    print(find_char("aAbEefIijOopUus"))

if __name__ == "__main__":
    main()
