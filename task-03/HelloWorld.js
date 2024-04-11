function isPrime(num) {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

function findPrimes(n) {
    const primes = [];
    for (let num = 2; num <= n; num++) {
        if (isPrime(num)) primes.push(num);
    }
    return primes;
}

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter a number: ', (n) => {
  console.log(`Prime numbers up to ${n} are: ${findPrimes(parseInt(n)).join(', ')}`);
  rl.close();
});
