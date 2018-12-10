def get_country_codes(prices):
    # your code here
    
    """ Return a string of country codes from a string of prices """
    
#_________________# 1. Break the string into a list. 
    prices = prices.split('$') # breaks the list into a list of elements.
    
#_________________# 2. Manipulate the individual elements.

    #_________________# A. Remove integers
#    nation = prices[0], prices[1]
    length = len(prices)

    for nation in (prices):
        nation == prices[0:]
    print(nation)
    #_________________# B.
    
    nations = []
    for each_char in (0, prices, 2):
        if each_char in prices[0:2]:
            nation = each_char
            nations = list(nations)
    #        lastitem = nations.pop()
    print(nations)


#_________________# 3. Make it back into a string.
#    set = [] 
#    my_list = ["happy"]
#    my_str = my_list[0][3:]
#    my_str == 'py' # True ## Jonathan's example from slack
    

#    print(" ".join(prices))

# don't include these tests in Vocareum
