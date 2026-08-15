# Counts and lists all prime numbers up to a user-defined limit.
def is_prime(number):
    '''Return True if the given number is prime, otherwise False.'''
    if number < 2:
        return False
    limit = int(number ** 0.5) + 1
    for divisor in range(2, limit):
        if number % divisor == 0:
            return False
    return True


try:
    limit = int(input('Enter the upper limit:'))
    if limit <= 0:
        raise ValueError
    prime_numbers = []
    for n in range(1, limit+1):
        if is_prime(n):
            prime_numbers.append(n)
    count = len(prime_numbers)
    print(f"There are {count} prime numbers in the range of {limit}")
    print(prime_numbers)
except ValueError:
    print("Invalid input. Please enter a natural number.")
