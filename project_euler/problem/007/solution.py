# 10,001st Prime Number

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

def solve(n):
    primes = [2]
    prime_count = 1

    cur = 2
    while prime_count < n:
        is_prime = True

        for prime in primes:
            if not is_prime: break

            if cur % prime == 0:
                is_prime = False

        if is_prime:
            primes.append(cur)
            prime_count = primes.__len__()

        cur += 1
    return primes

n_test_case = 6
n_question = 10_001

actual = solve(n_question)

print(actual)
print(f'last prime: {actual.pop()}')
