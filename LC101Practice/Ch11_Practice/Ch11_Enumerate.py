##___________ENUMERATE can be used to iterate through data collections. 

# Instead of this:

tennis_champs = ["Serena Williams", "Simona Halep", "Caroline Wozniacki",
    "Angelique Kerber", "Elina Svitolina"]
index = 1
for competitor in tennis_champs:
    print(index, competitor)
    index += 1

# Try this:

tennis_champs = ["Serena Williams", "Simona Halep", "Caroline Wozniacki",
    "Angelique Kerber", "Elina Svitolina"]

for idx, item in enumerate(tennis_champs):
      print(idx, item)

#Oops Serena shows as 0th place! Fix that by changing the range.

tennis_champs = ["Serena Williams", "Simona Halep", "Caroline Wozniacki",
    "Angelique Kerber", "Elina Svitolina"]

for index, competitor in enumerate(tennis_champs, 1):
      print(index, competitor)

# Now make it into a DICTIONARY:
tennis_champs = ["Serena Williams", "Simona Halep", "Caroline Wozniacki",
    "Angelique Kerber", "Elina Svitolina"]

champs_dictionary = dict(enumerate(tennis_champs, 1))

print(champs_dictionary)


# Or store them in a LIST OF TUPLES:
tennis_champs = ["Serena Williams", "Simona Halep", "Caroline Wozniacki",
    "Angelique Kerber", "Elina Svitolina"]

champs_tuples = list(enumerate(tennis_champs, 1))

print(champs_tuples)