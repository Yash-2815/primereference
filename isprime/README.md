# isprime

This folder contains programs to determine whether a number is prime using various methods.

## Programs
1. **primenumber.c**:
   - Implements multiple approaches for checking primality:
     - **Approach 1**: Brute force (check divisors from 2 to n-1).
     - **Approach 2**: Improved brute force (check divisors from 2 to n/2).
     - **Approach 3**: Optimized approach (check divisors up to √n).
     - **Approach 4**: Optimized with the 6k ± 1 rule.
   - Time complexities:
     - Approach 1: O(n)
     - Approach 2: O(n/2)
     - Approach 3: O(√n)
     - Approach 4: O(√n) (fewer checks compared to Approach 3).
   - Space complexity: O(1) (constant space usage).
2. **primes.py**:
   - Implements the same four approaches in Python for checking primality.
   - Time and space complexities are identical to those of `primenumber.c`.


