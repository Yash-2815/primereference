import math  # For mathematical operations like sqrt

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    # Check divisors from 2 to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:  # If divisible, not a prime number
            return False
    return True  # No divisors found, it's a prime number

# Function to find all prime factors of a number
def prime_factors(n):
    factors = []  # To store all factors
    prime_factors_list = []  # To store only prime factors

    # Find all factors of the number
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:  # If i divides n, add i to factors
            factors.append(i)
            if n // i != i:  # Avoid adding square root twice for perfect squares
                factors.append(n // i)

    # Filter prime factors from the list of all factors
    for factor in factors:
        if is_prime(factor):  # Check if the factor is prime
            prime_factors_list.append(factor)

    return prime_factors_list  # Return the list of prime factors

n = int(input("ENTER THE NUMBER: "))

 # Find and print the prime factors
print("PRIME FACTORS:", prime_factors(n))
