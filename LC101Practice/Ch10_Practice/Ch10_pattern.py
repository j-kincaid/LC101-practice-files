def primes_up_to(n):
    """ Return a list of all prime numbers less than n. """
    result = []  # initialize a result variable empty list
    for i in range(2, n): # loop
        if is_prime(i): # create new element
            result.append(i) # append the new element to the result
    return result