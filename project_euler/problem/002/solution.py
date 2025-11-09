# Even Fibonacci Numbers

def solve(n_fib_max):
    sum = 0
    previous, current = 0, 1

    while current < n_fib_max:
        next = get_next_fib(current, previous)
        previous, current = current, next

        if current % 2 == 0:
            sum += current

    return sum

def get_next_fib(current, previous):
    if previous == 0:
        return 2
    
    return current + previous

n_test_case = 89
n_question = 4_000_000

actual = solve(n_question)

print(actual)