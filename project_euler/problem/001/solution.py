# Multiples of 3 or 5

def solve(n):
    sum = 0

    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum

n_test_case = 10
n_question = 1000

actual = solve(n_question)

print(actual)