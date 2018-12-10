
#
# 
#_______________SPARSE MATRICES__________



matrix = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 3, 0]]

# Only 3 items here are nonzero. 
# Here's a dictionary representation of
# the same thing:
# matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
# Each key is a tuple and each value is an integer. 
# element_one = matrix[(0, 3)] # nested list representation

matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
print(matrix.get((0,3)))

print(matrix.get((1, 3), 0))

# Create the sparse matrix using a dictionary
for i in range(5):
    for j in range(5):
        print(matrix.get((i, j), 0), "", '')
    print()