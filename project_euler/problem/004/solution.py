# Largest Palindrome Product

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def solve():
    a, b = 100, 100
    max_palindrome = 0

    while a < 1_000:
        while b < 1_000:
            product = a * b
            if product > max_palindrome and is_palindrome(a * b):
                max_palindrome = product
            b += 1

        b = 100
        a += 1
    
    return max_palindrome

def is_palindrome(n):
    n_str = str(n)
    for i in range(0, n_str.__len__()//2):
        if not n_str[i] == n_str[n_str.__len__() - (1 + i)]:
            return False
    
    return True

actual = solve()

print(actual)