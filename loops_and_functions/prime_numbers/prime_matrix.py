# Finds prime numbers up to a user-defined limit and displays them
# grouped into rows of three, forming a matrix.
def build_prime_matrix(limit):
    """Find prime numbers below the given limit and group them into rows of three."""
    matrix = []
    row = []
    for number in range(1, limit+1):
        # Skip numbers smaller than 2
        if number < 2:
            continue
        # Skip even numbers except 2
        elif number % 2 == 0 and number != 2:
            continue
        # Only check divisor up the square root of the numbrer
        limit = int(number ** 0.5) + 1
        for divisor in range(2, limit):
            if number % divisor == 0:
                break
        else:
            # Runs only if no divisor broke the loop → number is prime
            row.append(number)
            # Group primes into rows of three
            if len(row) == 3:
                matrix.append(row)
                row = []
    # Append the remaining prime numbers
    if row:
        matrix.append(row)
    return matrix


try:
    limit = int(input("Enter the upper limit: "))
    if limit <= 0:
        raise ValueError
    prime_matrix = build_prime_matrix(limit)
    for row in prime_matrix:
        print(row)
except ValueError:
    print("Invalid input. Please enter a natural number.")
