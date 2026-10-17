# list refresher
# function to refresh basic list data structures
def list_test(name_lst_arg, num_lst_arg):
    name_lst = name_lst_arg
    print(name_lst)

list_test(["naem", "akthar", "hi", "hello", "are", "you!"], [3, 4, 8, 7, 6, 11])

num_lst = [1, 7, 8, 4, 3, 9, 10]
print(len(num_lst))

# list with mixed data types
mixed_lst = [1, 2, True, "apple", 4.8]
print(len(mixed_lst))

# accessing the list using the index
print(mixed_lst[3])

# access using negative index
print(mixed_lst[-1])

# access the list with range of index
print(mixed_lst[1:4])

# access the list with range of negative index
print(mixed_lst[-4:-1])

# change the list item with index
mixed_lst[0] = 10
print(mixed_lst)

# appending the list
mixed_lst.append(12)
print(mixed_lst)

# inserting into the list
mixed_lst.insert(0, 100)
print(mixed_lst)

# extending the list
tmp_lst = ["hi", "hello"]
mixed_lst.extend(tmp_lst)
print(mixed_lst)

# removing from the list
mixed_lst.remove(100)
mixed_lst.remove(10)
print(mixed_lst)

# poping from the list end
mixed_lst.pop()
mixed_lst.pop()
print(mixed_lst)

# looping through the list
for i in mixed_lst:
    print(i)

# loop through the index num
for i in range(len(mixed_lst)):
    print("--------")
    print(i)
    print(mixed_lst[i])
    print("--------")

# loop the list using the while loop
i =0
while i in range(len(mixed_lst)):
    print("-------")
    print(mixed_lst[i])
    i = i + 1

# looping the list using list comprehension
[print(i) for i in mixed_lst]

# append using list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_lst = [x for x in fruits if "a" in x]
print(new_lst)

# sorting the list - ascending order
test_lst = [7, 38, 0, 1, 77, 12, 25]
test_lst.sort()
print(test_lst)

# sorting the list - descending order
test_lst.sort(reverse=True)
print(test_lst)

# reverse the list
test_lst.reverse()
print(test_lst)

# copying the list
# direct copy is not possible in list like - list1 = list2

# copy using the list() keyword
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
tmp_fruits = list(fruits)
print(tmp_fruits)

# copy using .copy method
tmp_fruits_1 = fruits.copy()
print(tmp_fruits_1)

# copy using the slice operator
tmp_fruits_2 =fruits[:]
print(tmp_fruits_2)

# join the list
tmp_fruits_3 = tmp_fruits_1 + tmp_fruits_2
print(tmp_fruits_3)

# extend the list
number_lst = [1, 2, 3]
number_lst.extend([4, 5, 6])
print(number_lst)