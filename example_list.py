# showcase Python list methods
my_list = [1, 2, 3, 4, 5]

# append() - Adds an element to the end of the list
my_list.append(6)
print(my_list)

# extend() - Adds all elements from another list to the end of the list
my_list.extend([7, 8, 9])
print(my_list)

# insert() - Inserts an element at a specific index
my_list.insert(0, 0)
print(my_list)

# remove() - Removes the first occurrence of an element from the list
my_list.remove(3)
print(my_list)

# pop() - Removes and returns the element at a specific index
popped = my_list.pop(0)
print(popped)
print(my_list)

# index() - Returns the index of the first occurrence of an element
print(my_list.index(5))

# count() - Returns the number of occurrences of an element in the list
print(my_list.count(5))

# sort() - Sorts the elements of the list in ascending order
my_list.sort()
print(my_list)

# reverse() - Reverses the order of the elements in the list
my_list.reverse()
print(my_list)