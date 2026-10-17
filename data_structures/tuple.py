# tuple refresher
test_tuple = (1, 2, 3)
print(test_tuple)

# tuple length
length = len(test_tuple)
print(length)

# tuple allow duplicates
fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(fruits)

# accessing the tuple
test_tuple_number = (1, 2, 3, 6, 8)
print(test_tuple_number[3])

# negative indexing
print(test_tuple_number[-1])

# range of indexing
print(fruits[2:4])
print(fruits[:4])
print(fruits[::2])

# check if item exist in tuple
for i in fruits:
    if i == "apple":
        print("Yes there is fruit: " + i)


# tuple are immutable, so if we want to update the values in tuple, we need change to list and then back to tuple
tmp_list = list(fruits)
tmp_list[3] = "kiwi"
tmp_list[4] = "strawberry"
fruits = tuple(tmp_list)
print(fruits)

# tuples can be added to tuple
tmp_tuple_basket = ("orange", )
fruits = fruits + tmp_tuple_basket
print(fruits)

# unpacking a tuple
(green, yellow, red, orange, blue, brown) = fruits
print(green)
print(yellow)
print(red)

# unpacking with asterisk
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# looping through the tuple
for i in fruits:
    print(i)

# looping through index numbers
for i in range(len(fruits)):
    print(fruits[i])

# joining two tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)