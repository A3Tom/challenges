# Lattice Paths

# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner
#  _ _ _
# |_|_|_|   3 x 3
# |_|_|_|   (3+3)! / 3! * 3!
# |_|_|_|
# 
# How many such routes are there through a 20*20 grid?

def solve(x, y): 
    return int((factorial((x + y))) / (factorial(x) * factorial(y)))

def factorial(n):
    return arr_product([i for i in range(1, n + 1)])

def arr_product(array):
    result = 1
    for i in array:
        result *= i

    return result

n_test_case = 2
n_question = 20

actual = solve(n_question, n_question)

print(actual)