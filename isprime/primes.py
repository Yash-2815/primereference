import math

# Approach 1: Check divisors from 2 to n-1
def is_prime_approach1(n):
    if n <= 1:  # Numbers <= 1 are not prime
        return False
    for i in range(2, n):  # Check divisors from 2 to n-1
        if n % i == 0:  # If divisible, not a prime
            return False
    return True  # No divisors found, it's a prime

# Approach 2: Check divisors from 2 to n/2
def is_prime_approach2(n):
    if n <= 1:  # Numbers <= 1 are not prime
        return False
    for i in range(2, n // 2 + 1):  # Check divisors from 2 to n/2
        if n % i == 0:  # If divisible, not a prime
            return False
    return True  # No divisors found, it's a prime

# Approach 3: Check divisors from 2 to sqrt(n)
def is_prime_approach3(n):
    if n <= 1:  # Numbers <= 1 are not prime
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # Check divisors up to sqrt(n)
        if n % i == 0:  # If divisible, not a prime
            return False
    return True  # No divisors found, it's a prime

# Approach 4: Optimized with 6k ± 1 rule
def is_prime_approach4(n):
    if n <= 1:  # Numbers <= 1 are not prime
        return False
    if n == 2 or n == 3:  # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # Eliminate multiples of 2 and 3
        return False
    # Check divisors in the form of 6k ± 1 up to sqrt(n)
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True  # No divisors found, it's a prime

# Input number
n = int(input("ENTER THE NUMBER TO CHECK: "))
    
# Display approach options
print("CHOOSE AN APPROACH TO CHECK PRIME:")
print("1: Check divisors from 2 to n-1")
print("2: Check divisors from 2 to n/2")
print("3: Check divisors from 2 to sqrt(n)")
print("4: Optimized with 6k ± 1 rule")
    
# Input choice
choice = int(input("ENTER YOUR CHOICE (1-4): "))
    
# Determine if the number is prime using the selected approach
if choice == 1:
    result = is_prime_approach1(n)
elif choice == 2:
    result = is_prime_approach2(n)
elif choice == 3:
    result = is_prime_approach3(n)
elif choice == 4:
    result = is_prime_approach4(n)
else:
    print("INVALID CHOICE! Please choose a number between 1 and 4.")
    return
    
# Output the result
if result:
    print(f"\"{n}\" IS A PRIME NUMBER")
else:
    print(f"\"{n}\" IS NOT A PRIME NUMBER")


