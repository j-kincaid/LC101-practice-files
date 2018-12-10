def sum_all(nums):
    # your code here
    found_first = False
    total = 0
    
    for n in nums:
        if not found_first and n % 2 ==0:
            found_first = True
            continue
            
        total += n
        
    return total

print(sum_all([1,2,3,4]))
      
from test import testEqual

testEqual(sum_of_initial_odds([1,3,1,4,3,8]), 5)
testEqual(sum_of_initial_odds([6,1,3,5,7]), 0)
testEqual(sum_of_initial_odds([1, -7, 10, 23]), -6)
testEqual(sum_of_initial_odds(range(1,555,2)), 76729)