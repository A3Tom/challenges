#  43 44 45 46 47 48 49
#  42 21 22 23 24 25 26
#  41 20  7  8  9 10 27
#  40 19  6  1  2 11 28
#  39 18  5  4  3 12 29
#  38 17 16 15 14 13 30
#  37 36 35 34 33 32 31
#  1 = 1
#  2 = 3 x 3
#  3 = 5 x 5
#  4 = 7 x 7
#  x = x-1 x x-1
#  Corner sum = 4n^2 - 6(n-1)

# 81, 73, 65, 57 | 8 16 24 = 48
# 49, 43, 37, 31 | 6 12 18 = 36
# 25, 21, 17, 13 | 4 8 12 = 24

import math

def solve(n):
    result = [1] + [calc_corner_sum(i) for i in range(3, n+1, 2)]
    return sum(result)

def calc_corner_sum(n):
    return int((4 * math.pow(n, 2)) - (6 * (n - 1)))

n_test_case = 5
n_question = 1001

actual = solve(n_question)
print(actual)