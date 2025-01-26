#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm> // For sort and unique
using namespace std;

// Function to check if a number is prime
bool isPrime(long long n) {
    if (n <= 1) { // Numbers <= 1 are not prime
        return false;
    }
    // Check divisors from 2 to sqrt(n)
    for (long long i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) { // If divisible, not a prime
            return false;
        }
    }
    return true; // No divisors found, it's a prime number
}

// Function to find all prime factors of a number
vector<long long> primeFactors(long long n) {
    vector<long long> factors;        // To store all factors
    vector<long long> primeFactors;  // To store only prime factors

    // Find all factors of the number
    for (long long i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) { // If i divides n, add i to factors
            factors.push_back(i);
            if (n / i != i) { // Avoid adding square root twice for perfect squares
                factors.push_back(n / i);
            }
        }
    }

    // Filter prime factors from the list of all factors
    for (long long factor : factors) {
        if (isPrime(factor)) { // Check if the factor is prime
            primeFactors.push_back(factor);
        }
    }

    // Remove duplicates and sort the prime factors
    sort(primeFactors.begin(), primeFactors.end());
    primeFactors.erase(unique(primeFactors.begin(), primeFactors.end()), primeFactors.end());

    return primeFactors; // Return the vector of prime factors
}

int main() {
    // Input number from user
    long long n;
    cout << "ENTER THE NUMBER: ";
    cin >> n;

    // Find and display the prime factors
    vector<long long> result = primeFactors(n);
    cout << "PRIME FACTORS: ";
    for (long long factor : result) {
        cout << factor << " ";
    }
    cout << endl;

    return 0;
}
