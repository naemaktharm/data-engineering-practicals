# Python set refresher
test_set = {"apple", "banana", "cherry"}
print(test_set)

# Set means unordered, so each the elements retrieved can be different order
print(test_set)

# Set items can not be changed using index after the set is created


# duplicate items will be ignored
this_set = {"apple", "banana", "cherry", "apple"}
print(this_set)

#True and 1 is considered the same value:
this_set = {"apple", "banana", "cherry", True, 1, 2}
print(this_set)

# False and 0 is considered the same value:
this_set = {"apple", "banana", "cherry", False, True, 0}
print(this_set)

# length of the set
print(len(this_set))

# Access Items are not possible using index or key
# Set items can only be retrieved with the looping
for i in this_set:
    print(i)

# Set can be updated with function add()
this_set.add("avocado")
print(this_set)

# adding set to the set
this_set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
this_set.update(tropical)
print(this_set)

# adding any iterable
this_set = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange", 1]
this_set.update(mylist)
print(this_set)

# removing the element from set
this_set.remove(1)
print(this_set)

# removing the element from set using discard
this_set.discard("kiwi")
print(this_set)

# removing the random item using pop
this_set.pop()
print(this_set)

# delete the entire set using del keyword
# del this_set
# print(this_set) - this will fail

# looping through the set
for i in this_set:
    print(i)

# union() returns a new set with items from both sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# join two sets with |
set4 = set1 | set2
print(set4)

# join multiple sets
set5 = set1.union(set2, set3, set4)
print(set5) # will remove the distinct values

# update() method inserts all items from one set into another.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# intersection - return a new set with items present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# & - return a new set with items present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# immutable version of the set
x = frozenset({"apple", "banana", "cherry"})
print(x)
