def isprime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        
    return True


def gcd(a, b):
    """Compute the greatest common divisor using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a    


def isperfect(number):
    """
    Checks whether the given number is a perfect number.

    A perfect number is a positive integer that is equal to the sum of its proper divisors,
    excluding itself. For example, 6 is a perfect number because 1 + 2 + 3 = 6.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if the number is perfect, False otherwise.
    """
    """Check if a number is a perfect number."""
    if number < 1:
        return False
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisors_sum == number



