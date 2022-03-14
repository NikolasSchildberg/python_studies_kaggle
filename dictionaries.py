# Building, assigning and changing
twices = {
    'one': 1,
    'two': 2
}
twices['eight'] = 9
twices['eight'] = 8
print(twices)

# Dictionary comprehension, checking for key in dic
twices = { 'twice_'+number : 2 * twices[number] for number in twices }
print(twices)
print('twice_eight in twices:','twice_eight' in twices)

# Looping over keys and values
for kee in twices:
    print('{1} : {0}'.format(twices[kee],kee))
