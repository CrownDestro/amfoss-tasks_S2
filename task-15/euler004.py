t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    def largest_palindrome_less_than(limit):
        largest_palindrome = 0
        # Iterate over the range of 999 to 100 in reverse order
        for i in range(999, 99, -1):
            # Iterate over the range from i down to 100 in reverse order
            for j in range(i, 99, -1):
                product = i * j
                if product < limit and is_palindrome(product):
                    largest_palindrome = max(largest_palindrome, product)
                    break
        return largest_palindrome

    test_cases = [n]
    for limit in test_cases:
        result = largest_palindrome_less_than(limit)
        print(result)