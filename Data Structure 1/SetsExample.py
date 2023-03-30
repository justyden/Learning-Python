# Sets are unordered and an index can not be used to get data.
# Useful for determining similarties between sets or differences in sets.

set1 = {1, 2, 3}
print(set1)

set2 = {1, 1.0, "hi", (1, 2, 3)}
print(set2)

set3 = set([1, 2, 3, 2])  # Set constructor that can be used to create a set.
print(set3)

for each in set("That was good"):
    print(each)

for each in set2:  # Each time it prints the order can be different from the last.
    print(each)

set4 = {1, 2, 3}
print(set4)
set4.add(5)
print(set4)
set4.update([2, 3, 4, 6])
print(set4)
set4.add((1, 2, 8))
print(set4)
# Updates existing data and can take tuple or list.
set4.update(['a', 'b'], ('a', 'c'))
print(set4)
set4.update((1, 2, 7))  # Also updates this data into the set.
print(set4)
set4.add((1, 2, 7))  # Adds the tuple into the set.
print(set4)
set4.add((1, 2, 7))  # Trys to add tuple into set but it already exists.
print(set4)

set5 = {1, 2, 3, 4, 5, 6}
set5.discard(6)
print(set5)
# Discard can be used even if the element does not exist within the set.
set5.discard(6)
print(set5)
# Remove will throw and error if the element is not within the set.
set5.remove(5)
print(set5)

set6 = {1, 2, 3, 4, 5}
set7 = {4, 5, 6, 7, 8, 9}
print(set6 | set7)  # This is the symbol for union in python.
print(set6.union(set7))  # All do the same thing.
print(set7.union(set6))

# This is the symbol for intersection that is used in python.
print(set6 & set7)
print(set6.intersection(set7))  # All do the same thing.
print(set7.intersection(set6))

# This is for finding the difference between sets.
print(set6 - set7)  # These both are the same.
print(set6.difference(set7))

# This is also finds the difference but will give a different result.
print(set7 - set6)  # These both are the same.
print(set7.difference(set6))

# This is for finding elements in each set but not in both.
# Symmetric difference of sets.
print(set6 ^ set7)  # This is the symbol to use it in python.
print(set6.symmetric_difference(set7))  # These all are the same thing.
print(set7 ^ set6)
print(set7.symmetric_difference(set6))

set8 = frozenset([1, 2, 3, 4])
set9 = frozenset([3, 4, 5, 6])
set10 = frozenset([6, 7, 8, 9])  # These sets are immutable.
print(set8.isdisjoint(set9))
print(set8.difference(set9))
# Finds out if anything is in common between the sets.
# Returns true if nothing is in common between the sets.
print(set8.isdisjoint(set10))
