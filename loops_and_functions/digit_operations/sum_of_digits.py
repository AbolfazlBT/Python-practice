# Calculates the sum of the digits of a number using three different approaches.

def sum_of_digits_iterative(number):
    """Sum the digits of a number using a while loop."""
    number = abs(number)
    digits_sum = 0
    while number > 0:
        last_digit = number % 10
        digits_sum += last_digit
        number = number // 10
    return digits_sum


def sum_of_digits_generator(number):
    """Sum the digits of a number using a generator expression with sum()."""
    return sum(int(ch) for ch in str(abs(number)))


def sum_of_digits_recursive(n):
    """Sum the digits of a non-negative number using recursion (adds the last digit to the sum of the rest)."""
    if n == 0:
        return 0
    return n % 10 + sum_of_digits_recursive(n // 10)


try:
    number = int(input("Enter a number: "))

    print(
        f"Sum of digits (iterative method): {sum_of_digits_iterative(number)}")
    print(
        f"Sum of digits (generator method): {sum_of_digits_generator(number)}")
    print(
        f"Sum of digits (recursive method): {sum_of_digits_recursive(abs(number))}")
except ValueError:
    print("The entered value is invalid.")
