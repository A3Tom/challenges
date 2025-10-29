# Amicable Numbers

import math

def solve(n):
    d = {}
    amicable_pairs = []

    i = 2
    while i <= n:
        if amicable_pairs.__contains__(i):
            i += 1
            continue

        i_sum = d.get(i)

        if i_sum is None:
            i_sum = get_sum_of_factors(i)
            d[i] = i_sum
        
        if i == i_sum:
            i += 1
            continue

        i_sum_fs = d.get(i_sum)

        if i_sum_fs is None:
            i_sum_fs = get_sum_of_factors(i_sum)
            d[i_sum] = i_sum_fs

        if i == i_sum_fs:
            amicable_pairs.append(i_sum)
            amicable_pairs.append(i_sum_fs)

        i += 1

    return {
        'pairs': amicable_pairs, 
        'result': sum(amicable_pairs)
    }

def get_sum_of_factors(n): return sum(get_factors(n))

def get_factors(n):
    divisor_l = []

    median_divisor = math.floor(math.sqrt(n))
    for i in range(1, median_divisor + 1):
        div_result = n / i

        if (div_result).is_integer():
            if div_result != n:
                divisor_l.append(int(div_result))

            if i != int(div_result):
                divisor_l.append(i)

    return divisor_l

n_test_case = 284
n_question = 10_000

actual = solve(n_question)
print(actual)