people = [
    {"name": "Eldegard", "house": "Black Eagles"},
    {"name": "Dimitri", "house": "Blue Lions"},
    {"name": "Claude", "house": "Golden Deer"}
]

# Python doesn't know how to compare the above items!
# people.sort()

print(people)

# function to be used in the 'sort'
def f(person):
    return person["name"]

people.sort(key=f)

print(people)

# another way to implement this (inline lambda function)
people.sort(key=lambda person: person["name"])
print(people)