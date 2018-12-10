mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)
mylist.append(15)
print(mylist)
mylist.insert(3, 4)
print(mylist)
mylist.remove(27)
print(mylist)
mylist.reverse() 
print(mylist)
lastitem=mylist.pop() # removes and returns the last item
print(mylist)
print(lastitem)
mylist.index(12) # returns the position of the first occurrence of item
print(mylist.index(12))
print(mylist.count(4)) # count tells you how many times an item occurs in the list
mylist.append(29) # Adds a new item to the end of the list.
print(mylist)