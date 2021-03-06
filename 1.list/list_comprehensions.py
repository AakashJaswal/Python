# ORDERED, MUTABLE with DUPLICATE ELEMENTS
# Stack = FIFO, list can be used as stack using append and pop.
# list comprehension kinda works like lambda syntax
# syntax for list comprehension  = [output_expression for element in iterable if some_condition]

list1 = [1, 2, 3, 4, 5, 6]
list2 = [element + element
         for element in list1]
print(id(list1))
print(id(list2))
print(list2)

# i can also maybe make this dict ?
dict1 = {f'key{key}': key + 1
         for key in list1}
print(id(dict1))
print(dict1)
# Yes i can :D

# let's try to take sum and store it in dict key
sum_dict = {'Sum': 0}
y = lambda x, z: x + z
sum_dict = {'Sum': y(sum_dict['Sum'], val)
            for val in list1}

print(sum_dict)
# Interesting just take last result

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12], ]

transposed_matrix = [[row[i] for row in matrix]
                     for i in range(4)]
print(transposed_matrix)

flattened_matrix = [num
                    for row in matrix
                    for num in row]
print(flattened_matrix)

# ZIP loop over two sequence here list at a time
x_axis = [1, 3, 5, 7]
y_axis = [2, 4, 6, 8]
for x,y in zip(x_axis,y_axis):
    print(f"({x},{y})")
