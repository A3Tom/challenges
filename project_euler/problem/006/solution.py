# Sum Square Difference 

def solve(n):
    sum = 0
    sq_sum = 0
    for i in range(n + 1):
        sum += i
        sq_sum += pow(i, 2)

    print(f'sum: {sum} ({pow(sum, 2)}) sq sum: {sq_sum} diff: {pow(sum, 2) - sq_sum}')

    return pow(sum, 2) - sq_sum

n_test_case = 10
n_question = 100

actual = solve(n_question)

print(actual)