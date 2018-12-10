def double_stuff(alist):
    """ Overwrite each element in alist with double its value. """
    for position in range(len(alist)):
        alist[position] = 2 * alist[position] # Passing a list as an argument

def main():
    things = [2, 5, 9] # makes a reference to the original list, not a copy. 
    print(things)
    double_stuff(things)
    print(things)

if __name__ == "__main__":
    main()

    # These functions are called modifiers and the 
    # changes they make are called side effects. 
