# Detects generalized (nonconsecutive and nonclassical) patterns of length 3

# Finds the indexes of the flat steps (consecutive entries with the same value)
# in a sequence.
# Parameter: sequence, is a list.
# Return: a list of indexes.


def find_flat_steps(sequence):
    flat_steps = list()
    index = 0
    while index < len(sequence) - 1:
        if sequence[index] == sequence[index + 1]:
            flat_steps.append(index)
        index += 1
    return flat_steps

# Finds the indexes of the up steps in a sequence.
# Parameter: sequence, is a list.
# Return: a list of indexes.


def find_up_steps(sequence):
    up_steps = list()
    index = 0
    while index < len(sequence) - 1:
        if sequence[index] < sequence[index + 1]:
            up_steps.append(index)
        index += 1
    return up_steps

# Finds the indexes of the down steps in a sequence.
# Parameter: sequence, is a list.
# Return: True if t.


def find_down_steps(sequence):
    down_steps = list()
    index = 0
    while index < len(sequence) - 1:
        if sequence[index] > sequence[index + 1]:
            down_steps.append(index)
        index += 1
    return down_steps

# Given an index, a value and sequence, it determines if there is an entry in
# the sequence below the value, to the left of the index.
# Parameters: sequences is a list, value and index are integers.
# Return: a boolean.


def prev_low(sequence, index, value):
    for entry in sequence[:index]:
        if entry < value:
            return True
    return False

# Given an index, a value and sequence, it determines if there is an entry in
# the sequence equal to value, to the left of the index.
# Parameters: sequences is a list, value and index are integers.
# Return: a boolean.


def prev_equal(sequence, index, value):
    for entry in sequence[:index]:
        if entry == value:
            return True
    return False

# Given an index, a value and sequence, it determines if there is an entry in
# the sequence above the value, to the left of the index.
# Parameters: sequences is a list, value and index are integers.
# Return: a boolean.


def prev_high(sequence, index, value):
    for entry in sequence[:index]:
        if entry > value:
            return True
    return False

# Given an index, two values and sequence, it determines if there is an entry
# in the sequence between the values, to the left of the index. More
# specifically, if the entry is in the interval (value1, value2)
# Parameters: sequences is a list, value and index are integers.
# Return: a boolean.


def prev_between(sequence, index, value1, value2):
    for entry in sequence[:index]:
        if value1 < entry < value2:
            return True
    return False

# Given an index, a value and sequence, it determines if there is an entry in
# the sequence below the value, to the right of the index.
# Parameters: sequences is a list, value and index are integers.
# Return: a boolean.


def post_low(sequence, index, value):
    for entry in sequence[index + 1:]:
        if entry < value:
            return True
    return False

# Given an index, a value and sequence, it determines if there is an entry in
# the sequence equal to value, to the right of the index.
# Parameters: sequences is a list, value and index are integers.
# Return: a boolean.


def post_equal(sequence, index, value):
    for entry in sequence[index + 1:]:
        if entry == value:
            return True
    return False

# Given an index, a value and sequence, it determines if there is an entry in
# the sequence above the value, to the right of the index.
# Parameters: sequences is a list, value and index are integers.
# Return: a boolean.


def post_high(sequence, index, value):
    for entry in sequence[index + 1:]:
        if entry > value:
            return True
    return False

# Given an index, two values and sequence, it determines if there is an entry
# in the sequence between the values, to the right of the index. More
# specifically, if the entry is in the interval (value1, value2)
# Parameters: sequences is a list, value and index are integers.
# Return: a boolean.


def post_between(sequence, index, value1, value2):
    for entry in sequence[index + 1:]:
        if value1 < entry < value2:
            return True
    return False

# Detects the pattern 0-00 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect0_00(sequence):
    flats = find_flat_steps(sequence)
    for index in flats:
        if prev_equal(sequence, index, sequence[index]):
            return True
    return False

# Detects the pattern 1-00 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect1_00(sequence):
    flats = find_flat_steps(sequence)
    for index in flats:
        if prev_high(sequence, index, sequence[index]):
            return True
    return False

# Detects the pattern 1-10 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect1_10(sequence):
    downs = find_down_steps(sequence)
    for index in downs:
        if prev_equal(sequence, index, sequence[index]):
            return True
    return False

# Detects the pattern 1-01 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect1_01(sequence):
    ups = find_up_steps(sequence)
    for index in ups:
        if prev_equal(sequence, index, sequence[index + 1]):
            return True
    return False

# Detects the pattern 0-10 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect0_10(sequence):
    downs = find_down_steps(sequence)
    for index in downs:
        if prev_equal(sequence, index, sequence[index + 1]):
            return True
    return False

# Detects the pattern 0-11 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect0_11(sequence):
    flats = find_flat_steps(sequence)
    for index in flats:
        if prev_low(sequence, index, sequence[index]):
            return True
    return False

# Detects the pattern 0-01 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect0_01(sequence):
    ups = find_up_steps(sequence)
    for index in ups:
        if prev_equal(sequence, index, sequence[index]):
            return True
    return False

# Detects the pattern 00-0 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect00_0(sequence):
    flats = find_flat_steps(sequence)
    for index in flats:
        if post_equal(sequence, index + 1, sequence[index]):
            return True
    return False

# Detects the pattern 10-0 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect10_0(sequence):
    downs = find_down_steps(sequence)
    for index in downs:
        if post_equal(sequence, index + 1, sequence[index + 1]):
            return True
    return False

# Detects the pattern 11-0 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect11_0(sequence):
    flats = find_flat_steps(sequence)
    for index in flats:
        if post_low(sequence, index + 1, sequence[index + 1]):
            return True
    return False

# Detects the pattern 10-1 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect10_1(sequence):
    downs = find_down_steps(sequence)
    for index in downs:
        if post_equal(sequence, index + 1, sequence[index]):
            return True
    return False

# Detects the pattern 01-0 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect01_0(sequence):
    ups = find_up_steps(sequence)
    for index in ups:
        if post_equal(sequence, index + 1, sequence[index]):
            return True
    return False

# Detects the pattern 01-1 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect01_1(sequence):
    ups = find_up_steps(sequence)
    for index in ups:
        if post_equal(sequence, index + 1, sequence[index + 1]):
            return True
    return False

# Detects the pattern 00-1 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect00_1(sequence):
    flats = find_flat_steps(sequence)
    for index in flats:
        if post_high(sequence, index + 1, sequence[index + 1]):
            return True
    return False

# Detects the pattern 0-12 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect0_12(sequence):
    ups = find_up_steps(sequence)
    for index in ups:
        if prev_low(sequence, index, sequence[index]):
            return True
    return False

# Detects the pattern 2-01 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect2_01(sequence):
    ups = find_up_steps(sequence)
    for index in ups:
        if prev_high(sequence, index, sequence[index + 1]):
            return True
    return False

# Detects the pattern 2-10 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect2_10(sequence):
    downs = find_down_steps(sequence)
    for index in downs:
        if prev_high(sequence, index, sequence[index]):
            return True
    return False

# Detects the pattern 1-20 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect1_20(sequence):
    downs = find_down_steps(sequence)
    for index in downs:
        if prev_between(sequence, index, sequence[index + 1], sequence[index]):
            return True
    return False

# Detects the pattern 0-21 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect0_21(sequence):
    downs = find_down_steps(sequence)
    for index in downs:
        if prev_low(sequence, index, sequence[index + 1]):
            return True
    return False

# Detects the pattern 1-02 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect1_02(sequence):
    ups = find_up_steps(sequence)
    for index in ups:
        if prev_between(sequence, index, sequence[index], sequence[index + 1]):
            return True
    return False

# Detects the pattern 01-2 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect01_2(sequence):
    ups = find_up_steps(sequence)
    for index in ups:
        if post_high(sequence, index + 1, sequence[index + 1]):
            return True
    return False

# Detects the pattern 20-1 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect20_1(sequence):
    downs = find_down_steps(sequence)
    for index in downs:
        if post_between(sequence, index + 1, sequence[index + 1],
                        sequence[index]):
            return True
    return False

# Detects the pattern 21-0 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect21_0(sequence):
    downs = find_down_steps(sequence)
    for index in downs:
        if post_low(sequence, index + 1, sequence[index + 1]):
            return True
    return False

# Detects the pattern 12-0 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect12_0(sequence):
    ups = find_up_steps(sequence)
    for index in ups:
        if post_low(sequence, index + 1, sequence[index]):
            return True
    return False

# Detects the pattern 02-1 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect02_1(sequence):
    ups = find_up_steps(sequence)
    for index in ups:
        if post_between(sequence, index + 1, sequence[index],
                        sequence[index + 1]):
            return True
    return False

# Detects the pattern 10-2 in a sequence.
# Parameter: sequences is a list.
# Return: True if the pattern is found and False otherwise.


def detect10_2(sequence):
    downs = find_down_steps(sequence)
    for index in downs:
        if post_high(sequence, index + 1, sequence[index]):
            return True
    return False

# Detects a pattern in a sequence.
# Parameter: sequences is a list, pattern is a string.
# Return: True if the pattern is found and False otherwise.


def detect_pattern(sequence, pattern):
    if pattern == '0-00':
        return detect0_00(sequence)
    elif pattern == '1-00':
        return detect1_00(sequence)
    elif pattern == '1-10':
        return detect1_10(sequence)
    elif pattern == '1-01':
        return detect1_01(sequence)
    elif pattern == '0-10':
        return detect0_10(sequence)
    elif pattern == '0-11':
        return detect0_11(sequence)
    elif pattern == '0-01':
        return detect0_01(sequence)
    elif pattern == '00-0':
        return detect00_0(sequence)
    elif pattern == '10-0':
        return detect10_0(sequence)
    elif pattern == '11-0':
        return detect11_0(sequence)
    elif pattern == '10-1':
        return detect10_1(sequence)
    elif pattern == '01-0':
        return detect01_0(sequence)
    elif pattern == '01-1':
        return detect01_1(sequence)
    elif pattern == '00-1':
        return detect00_1(sequence)
    elif pattern == '0-12':
        return detect0_12(sequence)
    elif pattern == '2-01':
        return detect2_01(sequence)
    elif pattern == '2-10':
        return detect2_10(sequence)
    elif pattern == '1-20':
        return detect1_20(sequence)
    elif pattern == '0-21':
        return detect0_21(sequence)
    elif pattern == '1-02':
        return detect1_02(sequence)
    elif pattern == '01-2':
        return detect01_2(sequence)
    elif pattern == '20-1':
        return detect20_1(sequence)
    elif pattern == '21-0':
        return detect21_0(sequence)
    elif pattern == '12-0':
        return detect12_0(sequence)
    elif pattern == '02-1':
        return detect02_1(sequence)
    elif pattern == '10-2':
        return detect10_2(sequence)

# Counts the number of sequences in a collection that avoid a given pattern.
# Parameter: collection is a list of lists, pattern is a string.
# Return: an integer.


def count_avoid(collection, pattern):
    count = 0
    for sequence in collection:
        if not detect_pattern(sequence, pattern):
            count += 1
    return count

# Finds the sequences in a collection that avoid a given pattern.
# Parameter: collection is a list of lists, pattern is a string.
# Return: a list of lists.


def find_avoid(collection, pattern):
    avoiding = list()
    for sequence in collection:
        if not detect_pattern(sequence, pattern):
            avoiding.append(sequence)
    return avoiding
