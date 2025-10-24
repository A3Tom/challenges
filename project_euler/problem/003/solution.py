# Largest Prime Factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

def check_incremental(n):
    prime_factors = []
    cur = 1
    half_n = n//2

    while cur < half_n:
        if n % cur == 0 and is_prime(cur):
            prime_factors.append(cur)

        cur += 1

    return prime_factors

def factor_tree(n):
    prime_factors = []
    cur = n

    i = 2
    while i <= cur:
        if cur % i == 0:
            prime_factors.append(i)
            cur = cur / i
            i = 2
        else:
            i += 1
    return prime_factors


def is_prime(n):
    half_n = (n//2) + 1
    for i in range(2, half_n):
        if i > 2 and i % 2 == 0:
            continue
        if n % i == 0:
            return False
    return True

n_test_case = 13_195
n_question = 600_851_475_143

actual = factor_tree(n_question)
print(actual)
print(f'largest: {actual.pop()}')