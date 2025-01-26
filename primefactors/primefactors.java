import java.util.*; // For Scanner and ArrayList

class PrimeFactors {

    // Function to check if a number is prime
    boolean isPrime(long n) {
        if (n <= 1) { // Numbers less than or equal to 1 are not prime
            return false;
        }
        // Check divisors from 2 to sqrt(n)
        for (long i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) { // If divisible, not a prime number
                return false;
            }
        }
        return true; // No divisors found, it's a prime number
    }

    // Function to find all prime factors of a number
    long[] primeFactors(long n) {
        ArrayList<Long> factors = new ArrayList<>();  // To store all factors
        ArrayList<Long> primeFactors = new ArrayList<>(); // To store only prime factors

        // Find all factors of the number
        for (long i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) { // If i divides n, add i to factors
                factors.add(i);
                if (n / i != i) { // Avoid adding square root twice for perfect squares
                    factors.add(n / i);
                }
            }
        }

        // Filter prime factors from the list of all factors
        for (long factor : factors) {
            if (isPrime(factor)) { // Check if the factor is prime
                primeFactors.add(factor);
            }
        }

        // Convert the list of prime factors to an array
        long[] resultArray = new long[primeFactors.size()];
        for (int i = 0; i < primeFactors.size(); i++) {
            resultArray[i] = primeFactors.get(i);
        }

        return resultArray; // Return the array of prime factors
    }

    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner sc = new Scanner(System.in);
        
        // Prompt the user to enter a number
        System.out.println("ENTER THE NUMBER:");
        long n = sc.nextLong();

        // Create an instance of the PrimeFactors class
        PrimeFactors pf = new PrimeFactors();

        // Find and print the prime factors
        System.out.println("PRIME FACTORS: " + Arrays.toString(pf.primeFactors(n)));

        // Close the scanner to avoid resource leaks
        sc.close();
    }
}
