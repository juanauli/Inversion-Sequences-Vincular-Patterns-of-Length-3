# Finding and counting inversion sequences avoiding
# generalized (nonconsecutive and nonclassical) patterns of length 3
# Uses the file detect_gen_pattern3.py and gen_inv_seq.py


import detect_gen_pattern3
import gen_inv_seq

# Counts the number of inversion sequences of a given length
# that avoid a given pattern of length 3.
# Parameters: length is an integer, pattern is a string.
# Returns the number of inversion sequences of the given length
# that avoid the pattern, an integer.


def count_gen_inv_avoiding3(length, pattern):
    return detect_gen_pattern3.count_avoid(gen_inv_seq.inv_seq(length),
                                           pattern)

# Finds the inversion sequences of a given length that avoid
# a given pattern of length 3.
# Parameters: length is an integer, pattern is a string.
# Returns the inversion inversion sequences of the given length
# that avoid the pattern, a list.


def find_gen_inv_avoiding3(length, pattern):
    return detect_gen_pattern3.find_avoid(gen_inv_seq.inv_seq(length), pattern)
