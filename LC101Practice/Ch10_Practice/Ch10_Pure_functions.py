def double_stuff(alist):
    """ Return a new list in which contains doubles of the elements in alist. """
    new_list = []
    for value in alist:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

# A pure function does not produce side effects. 
def main():
    things = [2, 5, 9]
    print(things)
    things = double_stuff(things) 
    # Here we assign the 
    # return value back to things. 
    print(things)

if __name__ == "__main__":
    main()