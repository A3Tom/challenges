# Smallest Multiple

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
        


