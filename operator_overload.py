# trying to perform operator_overload in python,
# and using it to perform string concatenation when
# calling the sum function on a list of strings

print("Before:", sum([1, 2, 3]))


def sum(iterablee, sep=' '):
    result = ''
    for string in iterablee:
        result += string + sep
    return result


print(sum(['Die', 'Gedanken', 'sind', 'frei']))

# print("After:", sum([1, 2, 3]))
