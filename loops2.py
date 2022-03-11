testes = [
    [1, 2, 3, 4, 5],
    [-1, -10, -10000, -34, 3],
    [],
    [0, -1, 1]
]


def count_negatives(lista):
    count_negatives = 0
    for number in lista:
        if (number < 0):
            count_negatives += 1
    return count_negatives


def better_count_negatives(lista):
    return len([number for number in lista if number < 0])


def best(numbers):
    return sum([number < 0 for number in numbers])


# running tests
for lista in testes:
    print(
        count_negatives(lista),
        better_count_negatives(lista),
        best(lista)
    )
