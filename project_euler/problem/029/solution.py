import math

def solve(n):
    result = set()

    for i in range(2, n+1):
        for j in range(2, n+1):
            result.add(math.pow(i, j))
            result.add(math.pow(j, i))

    return len(result)

n_test_case = 5
n_question = 100

actual = solve(n_question)
print(actual)