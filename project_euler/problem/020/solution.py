# Factorial Digit Sum

def solve(n):
    fac_arr = [int(i) for i in str(factorial(n))]
    return sum(fac_arr)

def factorial(n):
    return arr_product([i for i in range(1, n + 1)])

def arr_product(array):
    result = 1
    for i in array:
        result *= i

    return result

n_test_case = 10
n_question = 100

actual = solve(n_question)
print(actual)