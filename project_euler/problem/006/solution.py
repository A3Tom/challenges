# Sum Square Difference 

# The sum of the squares of the first ten natural numbers is:
#     1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is: 
#     (1 + 2 + ... + 10)^2 = 55^2 = 3025.
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


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