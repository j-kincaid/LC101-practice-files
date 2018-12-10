def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    fullname = fullname.split()
    init = ""
    for name in fullname:
        init = init + name[0]
        init = init.upper()
    print(init)    
    return init
    

def main():
    fullname = input("Please enter your full name: ")
    get_initials()

if __name__ == "__main__":
    main()