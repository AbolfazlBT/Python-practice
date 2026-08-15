# Counts occurrences of target numbers in a list, using three different approaches.

import ast
from collections import Counter


def count_numbers_in_operator(lst, targets):
    """Counts occurrences of each target number using the in operator."""
    counts = {v: 0 for v in targets}
    for number in targets:
        if number in lst:
            counts[number] += 1
    return counts


def count_numbers_list_count(lst, targets):
    """Counts occurrences of each target number using list.count()."""
    counts = {v: lst.count(v) for v in targets}
    return counts


def count_numbers_counter(lst, targets):
    """Counts occurrences of each target number using collections.Counter."""
    counts = Counter(lst)
    counts_targets = {target: counts[target] for target in targets}
    return counts_targets


try:
    list_input = input(
        "Enter the list of numbers as integers (e.g. [3,3,6,89,65,65,12,26]): ")
    lst = ast.literal_eval(list_input)
    if not isinstance(lst, list):
        raise TypeError

    targets_input = input(
        "Enter the numbers to be counted, separated by commas (e.g. 3,6,78,8): ")
    targets_input = targets_input.strip('[]')
    targets = [int(x) for x in targets_input.split(',')]

    print(f"Counts (in operator): {count_numbers_in_operator(lst, targets)}")
    print(f"Counts (list.count): {count_numbers_list_count(lst, targets)}")
    print(f"Counts (Counter): {count_numbers_counter(lst, targets)}")
except ValueError:
    print('''
    The entered value is invalid.
    Please enter the value as described.
    ''')
except SyntaxError:
    print("The entered syntax is incorrect. Please pay attention to the input format.")
except TypeError:
    print("Invalid input type. The first value must be a list of numbers.")
