from itertools import permutations
def possible_permutations(numbers):

    for permutation in permutations(numbers):
        yield list(permutation)

    return permutation
[print(n) for n in possible_permutations([1, 2, 3])]