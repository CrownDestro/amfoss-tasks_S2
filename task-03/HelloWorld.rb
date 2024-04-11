def is_prime(num)
    return false if num < 2
    (2..Math.sqrt(num)).each do |i|
        return false if num % i == 0
    end
    true
end

def find_primes(n)
    primes = []
    (2..n).each do |num|
        primes << num if is_prime(num)
    end
    primes
end

print "Enter a number: "
n = gets.chomp.to_i
puts "Prime numbers up to #{n} are: #{find_primes(n)}"
