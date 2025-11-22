def solve(n):
    max_val = []
    max_idx = 0
    for i in range(2, n):
        val = get_decimal_list(i)

        if(len(val) > len(max_val)):
            max_val = val
            max_idx = i

    print(f'{max_idx} with {len(max_val)} digits')

def get_decimal_list(n):
    decimal_part = []
    remainders = set()

    rem = 1
    while True:
        div = rem // n
        rem = rem % n
        decimal_part.append(div)

        if rem == 0 or rem in remainders:
            break

        remainders.add(rem)
        rem *= 10

    return decimal_part[1:]

n_test_case = 11
n_question = 1000
actual = solve(n_question)