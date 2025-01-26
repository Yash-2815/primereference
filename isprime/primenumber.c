#include <stdio.h>
#include <stdbool.h>
#include <math.h> // For sqrt in approaches 3 and 4

// Approach 1: Check divisors from 2 to n-1
bool isPrimeApproach1(int n) {
    if (n <= 1) {
        return false; // Numbers <= 1 are not prime
    }
    for (int i = 2; i < n; i++) {
        if (n % i == 0) { // If divisible, not a prime
            return false;
        }
    }
    return true; // No divisors found, it's a prime
}

// Approach 2: Check divisors from 2 to n/2
bool isPrimeApproach2(int n) {
    if (n <= 1) {
        return false; // Numbers <= 1 are not prime
    }
    for (int i = 2; i <= n / 2; i++) {
        if (n % i == 0) { // If divisible, not a prime
            return false;
        }
    }
    return true; // No divisors found, it's a prime
}

// Approach 3: Check divisors from 2 to sqrt(n)
bool isPrimeApproach3(int n) {
    if (n <= 1) {
        return false; // Numbers <= 1 are not prime
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) { // If divisible, not a prime
            return false;
        }
    }
    return true; // No divisors found, it's a prime
}

// Approach 4: Optimized with 6k ± 1 rule
bool isPrimeApproach4(int n) {
    if (n <= 1) {
        return false; // Numbers <= 1 are not prime
    }
    if (n == 2 || n == 3) {
        return true; // 2 and 3 are prime
    }
    if (n % 2 == 0 || n % 3 == 0) {
        return false; // Multiples of 2 or 3 are not prime
    }
    // Check divisors in the form of 6k ± 1 up to sqrt(n)
    for (int i = 5; i <= sqrt(n); i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false; // If divisible, not a prime
        }
    }
    return true; // No divisors found, it's a prime
}

int main() {
    int n, choice;
    
    printf("ENTER THE NUMBER TO CHECK: ");
    scanf("%d", &n); // Input the number
    
    printf("CHOOSE AN APPROACH TO CHECK PRIME:\n");
    printf("1: Check divisors from 2 to n-1\n");
    printf("2: Check divisors from 2 to n/2\n");
    printf("3: Check divisors from 2 to sqrt(n)\n");
    printf("4: Optimized with 6k ± 1 rule\n");
    printf("ENTER YOUR CHOICE: ");
    scanf("%d", &choice); // Input the choice
    
    bool result = false;
    
    switch (choice) {
        case 1:
            result = isPrimeApproach1(n);
            break;
        case 2:
            result = isPrimeApproach2(n);
            break;
        case 3:
            result = isPrimeApproach3(n);
            break;
        case 4:
            result = isPrimeApproach4(n);
            break;
        default:
            printf("INVALID CHOICE! Please choose between 1 and 4.\n");
            return 0;
    }
    
    if (result) {
        printf("\"%d\" IS A PRIME NUMBER\n", n);
    } else {
        printf("\"%d\" IS NOT A PRIME NUMBER\n", n);
    }
    
    return 0;
}
