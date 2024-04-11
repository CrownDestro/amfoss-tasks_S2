package main

import (
    "fmt"
    "math"
)

func isPrime(num int) bool {
    if num < 2 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}

func findPrimes(n int) []int {
    primes := []int{}
    for num := 2; num <= n; num++ {
        if isPrime(num) {
            primes = append(primes, num)
        }
    }
    return primes
}

func main() {
    var n int
    fmt.Print("Enter a number: ")
    fmt.Scanln(&n)
    fmt.Printf("Prime numbers up to %d are: %v\n", n, findPrimes(n))
}
