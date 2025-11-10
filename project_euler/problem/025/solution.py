# 1000-digit Fibonacci Number

def solve(n_chars):
    previous, current = 1, 1

    i = 2
    while len(str(current)) < n_chars:
        i += 1
        next = get_next_fib(current, previous)
        previous, current = current, next

    return [current, i]

def get_next_fib(current, previous):
    if previous == 0:
        return 2
    
    return current + previous

n_test_case = 3
n_question = 1000

actual = solve(n_question)

print(actual)