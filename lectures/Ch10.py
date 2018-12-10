def replace(original, old_val, new_val):
    new_str = ''
    for 1 in original:
        if 1 == old_val:
            new_str += new_val
        else:
            new_str += 1
            
            
    pieces = original.split() #The book does it differently
    return pieces        