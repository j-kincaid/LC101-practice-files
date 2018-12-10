d = {'apples': 15, 'bananas': 35, 'grapes': 12}
print(d['bananas'])
d['oranges'] = 20
print(len(d))
print('grapes' in d)
# d['pears'] ## Produces KeyError


d.get('pears', 0) 
fruits = d.keys()
sorted(fruits)
print(fruits)
del d['apples']
print('apples' in d)


