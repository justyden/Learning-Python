list1 = [1, 5, 'a', "yes"]
print(list1[0])

list2 = [1, "more", 5.0, [1, 4, 10], 104]
print(list2[3][2])
print(list1 + list2)  # Can do addition and multiplication on lists.
print(list1 * 4)

a = "dog"
print(a * 4)
print(1 in list2)
# Checks the list and determines if the variable in question is in it.
print(4 in list2[3])

print(list1[0:2])  # This is splicing and it is inclusive then exclusive.

list3 = list1[1:]
print(list3)

list1[1] = 10
print(list1)

list1.append(100)
print(list1)

list1.append([1, 2, 3])
print(list1)

# Does not delete the list and create a new list but instead adds to the existing list
list1.extend(list3)
print(list1)

# Different methods to delete data from a list
num1 = list2.pop(2)
print(num1)
print(list2)

list2.pop()
print(list2)

del list2[1]
print(list2)

list4 = [1, 5, 10, 90]
list4.remove(5)
print(list4)

for item in list4:
    print(item)

list5 = [item ** 2 for item in list4]
print(list5)

list6 = [1, 4, 10, 15, 40]
del list6[1:3]
print(list6)
