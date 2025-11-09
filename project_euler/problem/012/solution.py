# Highly Divisible Triangular Number

import math

def solve(n):
    pyramid_n = 0
    cur = 1
    divisor_l = []

    while len(divisor_l) <= n:
        divisor_l = []
        pyramid_n += cur

        median_divisor = math.floor(math.sqrt(pyramid_n))

        for i in range(1, median_divisor + 1):
            div_result = pyramid_n / i

            if (div_result).is_integer():
                divisor_l.append(int(div_result))
                if i != int(div_result):
                    divisor_l.append(i)
    
        divisor_l.sort()
        cur += 1

    return pyramid_n

n_test_case = 5
n_question = 500

actual = solve(n_question)

print(actual)