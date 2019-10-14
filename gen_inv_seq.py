# Generates inversion sequences of a given length >= 1.
# Parameter: length is an integer.
# Return: inversion sequences of the given length, a list of lists.


def inv_seq(length):
    if length == 1:
        return [[0]]
    inversions = list()
    for a in range(length):
        for inv in inv_seq(length - 1):
            inversions.append(inv + [a])
    return inversions
