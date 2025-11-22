import math 

def solve(n):
    powers = build_power_cache(n)
    result = []

    for i in range(2, 1_000_000):
        i_pow = [powers[int(s)] for s in str(i)]
        if sum(i_pow) == i:
            result.append(i)

    return result


def build_power_cache(n):
    powers = [int(math.pow(i, n)) for i in range(0, 10)]
    return dict(list(enumerate(powers)))

n_test_case = 4
n_question = 5

actual = solve(n_question)
print(actual)
print(sum(actual))