# Summation of Primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Notes:
# This was very, very slow - if this comes up again this needs optimized

def solve(n):
    primes = [2]
    sum = 2

    cur = 2
    while cur < n:
        is_prime = True

        for prime in primes:
            if not is_prime: break

            if cur % prime == 0:
                is_prime = False

        if is_prime:
            primes.append(cur)
            sum += cur

        cur += 1

    print(primes)
    return sum

n_test_case = 10
n_question = 2_000_000

actual = solve(n_test_case)

print(actual)
