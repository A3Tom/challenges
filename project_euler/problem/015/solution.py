# Lattice Paths

# |_|_|_|   3 x 3
# |_|_|_|   (3+3)! / 3! * 3!
# |_|_|_|

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