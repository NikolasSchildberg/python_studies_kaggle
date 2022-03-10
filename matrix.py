my_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Printing matrix row by row
print("My matrix is")
for row in my_matrix:
    print(row)

# Printing matrix row after row in one line
print("\nor", my_matrix)

# Printing matrix in cooler formatting
print("\nAnd now everyone without squarebrackets")
for row in my_matrix:
    # print("\n")
    for item in row:
        if row.index(item) == len(row) - 1:
            print(item, end="\n")
        else:
            print(item, end=", ")
