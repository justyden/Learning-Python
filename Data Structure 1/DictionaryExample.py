dictionary1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dictionary1)

dictionary1['e'] = 5  # Inserting a new key value pair.
print(dictionary1)

# Inserting a key that exists replaces that key including the value.
dictionary1['b'] = 10
print(dictionary1)

print(dictionary1.keys())
print(dictionary1.values())
print(dictionary1.items())

del dictionary1['b']  # Deletes the key value pair according to the key.
print(dictionary1)

dictionary2 = {'a': 4, 'b': 5, 'c': 10}
# Does not delete the dictionary but instead clears all key value pairs.
dictionary2.clear()
print(dictionary2)

dictionary3 = {}
dictionary3[1] = 1
dictionary3['1'] = 2
dictionary3[1] += 1
dictionary3[1.0] = 4
# There is floats in python but it is smart enough to know if it can be
# converted to an integer without losing data.
sum1 = 0
print(dictionary3.items())
print(dictionary3.keys())
print(dictionary3.values())
for k in dictionary3:
    sum1 += dictionary3[k]
print(sum1)

# Anything that can be modified can not be a key in a dictionary.
dictionary4 = {}
dictionary4[(1, 2, 4)] = 8
dictionary4[(4, 2, 1)] = 10
dictionary4[(1, 2)] = 12
print(dictionary4)
sum2 = 0
for k in dictionary4:
    sum2 += dictionary4[k]
print(sum2)
# Using len gets the amount of key value pairs in the dictionary.
print(len(dictionary4) + sum2)

boxes = {}
jars = {}
crates = {}
boxes['food'] = 1
boxes['water'] = 2
jars['honey'] = 4
crates['boxes'] = boxes
crates['jars'] = jars
print(crates)
print(len(crates['boxes']))
