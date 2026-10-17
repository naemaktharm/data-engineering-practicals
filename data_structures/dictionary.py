# Dictionary refresher
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# access the items of dictionary using keys
print(car["brand"])
print(car["model"])
print(car["year"])

# dictionary keys
car_keys_value = car.keys()
print(car_keys_value)

# dictionary values
dict_values = car.values()
print(dict_values)

# get items
x = car.items()
print(x)

# changing the items in the dictionary
car["year"] = 1965
print(car)
car["year"] = 1964
print(car)

# adding the values to the dictionary
car["color"] = "red"
print(car)

# popping the values from dictionary
car.pop("color")
print(car)

# looping through the dictionary
for i in car:
    print(i)

# looping through the dictionary keys
for i in car.keys():
    print(i)

# looping through the dictionary values
for i in car.values():
    print(i)

# looping through the dictionary items
for x,y in car.items():
    print(x, y)

# Nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# retrieving the items from the dictionary
for i, obj in myfamily.items():
    print(i)

    for j in obj:
        print(obj[j])