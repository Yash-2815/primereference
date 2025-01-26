import math  # For mathematical operations like sqrt

# Function to find and print prime numbers up to 'n'
def sieve_of_eratosthenes(n):
    # Array to store whether each number is prime (1: prime, 0: not prime)
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0  # '0' and '1' are not prime numbers
    
    # Implementing the Sieve of Eratosthenes algorithm
    for i in range(2, int(math.sqrt(n)) + 1):  # Loop up to the square root of n
        if primes[i] == 1:  # If the number is still marked as prime
            # Mark all multiples of i as non-prime
            for j in range(i * i, n + 1, i):
                primes[j] = 0  # Mark multiples of i as not prime

    # Counting and printing the prime numbers
    prime_count = 0
    print(f"Prime numbers up to {n}:")
    for i in range(2, n + 1):
        if primes[i] == 1:  # If the number is prime
            print(i, end=" ")  # Print the prime number
            prime_count += 1  # Increment the prime count

    print()  # New line for better formatting
    print(f"Count of primes: {prime_count}")  # Print the total count of primes


# Get the maximum number from the user
n = int(input("Enter the maximum number to find primes: "))

# Call the sieve_of_eratosthenes function
sieve_of_eratosthenes(n)
