# Smallest Multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is divisible with no remainder by all of the numbers from 1 to 20?

def solve(n):
    i = 2
    while True:
        for j in range(1, n+1):
            if i % j != 0:
                break

            if j == n:
                return i
        i += 2

actual = solve(20)

print(actual)
        


