# Special Pythagorean Triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Notes

# Euclid's Formula:
# a = m^2 - n^2 | b = 2mn | c = m^2 + n^2
# m > n > 0

# m^2 - n^2 + m^2 + n^2 + 2mn = 1000
# 2m^2 + 2mn = 1000
# 2m^2 + 2mn = c
# 2m^2 + 2mn - c = 0
# 2mn = c - 2m^2
# mn = c/2 - m^2
# n = (c/2 - m^2) / m

def solve(triplet_sum):
    m, n = determine_components(triplet_sum)

    a = pow(m, 2) - pow(n, 2)
    b = 2 * m * n
    c = pow(m, 2) + pow(n, 2)

    sum = a + b + c
    product = a * b * c

    print(f'm: {m} | n: {n}')
    print(f'a: {a} | b: {b} | c: {c} (+{sum}) (*{product})')

    return product

def determine_components(triplet_sum):
    m, n = 2, 0
    while n == 0 and m < (triplet_sum / 2):
        x = (triplet_sum / 2 - pow(m, 2)) / m
        if m > x and float(x).is_integer():
            n = x
        else:
            m += 1
    return int(m), int(n)

n_test_case = 12
n_question = 1_000

actual = solve(n_question)
print(actual)