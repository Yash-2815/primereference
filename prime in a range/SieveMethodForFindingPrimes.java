import java.util.*; // For Scanner

public class SieveMethodForFindingPrimes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // Create a Scanner object for user input

        // Prompt user to input the maximum number (n)
        System.out.print("Enter the maximum number to find primes: ");
        int n = sc.nextInt();

        // Array to mark prime numbers
        int[] primes = new int[n + 1]; // Array to store prime status (1: prime, 0: not prime)
        primes[0] = 0; // '0' is not a prime number
        primes[1] = 0; // '1' is not a prime number

        // Initially assume all numbers from 2 to n are prime
        for (int i = 2; i <= n; i++) {
            primes[i] = 1; // Mark all numbers as prime (1: true)
        }

        // Sieve of Eratosthenes algorithm
        for (int i = 2; i * i <= n; i++) { // Loop up to the square root of n
            if (primes[i] == 1) { // If the number is still marked as prime
                // Mark all multiples of i as non-prime
                for (int j = i * i; j <= n; j += i) {
                    primes[j] = 0; // Set multiples of i to 0 (not prime)
                }
            }
        }

        int count = 0; // To count the number of primes
        System.out.println("Prime numbers up to " + n + ":");

        // Print all prime numbers and count them
        for (int i = 2; i <= n; i++) {
            if (primes[i] == 1) { // If the number is prime
                System.out.print(i + " "); // Print the prime number
                count++; // Increment the count of primes
            }
        }

        System.out.println(); // New line for better formatting
        System.out.println("Count of primes: " + count); // Print the total count of primes

        sc.close(); // Close the Scanner to avoid resource leaks
    }
}
