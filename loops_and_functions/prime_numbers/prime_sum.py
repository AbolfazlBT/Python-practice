# Calculates the sum of prime numbers up to a user-defined limit,
# using two different approaches (with and without a flag variable).
def sum_prime_with_flag(limit):
    """Sum all prime numbers up to the given limit, using a flag variable."""
    sum_prime = 0
    number = 2
    while number <= limit:
        is_prime = True
        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            sum_prime += number
        number += 1
        return sum_prime


def sum_prime_without_flag(limit):
    """Sum all prime numbers up to the given limit, relying on the loop condition instead of a flag."""
    sum_prime = 0
    number = 2
    while number <= limit:
        divisor = 2
        while divisor * divisor <= number and number % divisor != 0:
            divisor += 1
        if divisor * divisor > number:
            sum_prime += number
        number += 1
    return sum_prime


try:
    limit = int(input("Enter the upper limit: "))
    if limit <= 0:
        raise ValueError
    print(f"Sum of primes (with flag): {sum_prime_with_flag}")
    print(f"Sum of primes (without flag): {sum_prime_without_flag}")
except ValueError:
    print("Invalid input. Please enter a natural number.")
