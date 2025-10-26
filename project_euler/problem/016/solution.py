# Power Digit Sum

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

# I feel like I'm missing a golden tool to just plug an exponent into and it'll give the answer

def solve(n):
    sq = 0
    for i in range(1, n+1):
        sq = pow(2, i)
    ints = [int(x) for x in str(sq)]
    return sum(ints)

n_test_case = 15
n_question = 1000

actual = solve(n_question)

print(actual)