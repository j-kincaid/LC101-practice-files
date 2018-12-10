def get_initials(fullname):
    # some code heremy_name = "Edgar Allan Poe"

    user_name = input(‘Type your name and press ENTER: ’)
    name_list = user_name.split()
    init = ""
    for name in name_list:
        init = init + name[0]
    print(init)



if __name__ == ‘__main__‘:
   main()
def main():
    
    get_initials()
    # some more code here (input and print statements)

if __name__ == '__main__':
    main()

ozzie_inits = get_initials("Ozzie Smith")
print("The initials of 'Ozzie Smith' are", ozzie_inits)
# => prints "The initials of 'Ozzie Smith' are OS"
    