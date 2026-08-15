# Reverses the digits of a number using two different approaches.

def reverse_number_iterative(number):
    """Reverse the digits of a number using a while loop (handles negative numbers)."""
    is_negative = number < 0
    number = abs(number)
    reversed_number = 0
    while number > 0:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number = number // 10
    if is_negative:
        reversed_number = -reversed_number
    return reversed_number


def reverse_number_recursive(n, reversed_so_far=0):
    """Reverse the digits of a non-negative number using recursion (calls itself with one digit removed)."""
    if n == 0:
        return reversed_so_far
    reversed_so_far = reversed_so_far * 10 + n % 10
    n = n // 10
    return reverse_number_recursive(n, reversed_so_far)


try:
    number = int(input("Enter a number: "))
    is_negative = number < 0

    iterative_result = reverse_number_iterative(number)
    recursive_result = reverse_number_recursive(abs(number))
    if is_negative:
        recursive_result = -recursive_result

    print(f"Reversed numbr (iterative method): {iterative_result}")
    print(f"Reversed numbr (recursive method): {recursive_result}")
except ValueError:
    print("The entered value is invalid.")
