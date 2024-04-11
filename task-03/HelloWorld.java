import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class PrimeNumbers {
    public static boolean isPrime(int num) {
        if (num < 2) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }

    public static List<Integer> findPrimes(int n) {
        List<Integer> primes = new ArrayList<>();
        for (int num = 2; num <= n; num++) {
            if (isPrime(num)) primes.add(num);
        }
        return primes;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();
        List<Integer> primeNumbers = findPrimes(n);
        System.out.println("Prime numbers up to " + n + " are: " + primeNumbers);
        scanner.close();
    }
}
