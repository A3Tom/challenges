# Longest Collatz Sequence

def solve(n):
    max_chain = []

    for i in range(1, n+1):
        collatz_chain = get_collatz_chain(i)
        if len(collatz_chain) > len(max_chain):
            max_chain = collatz_chain
        
    return max_chain

def get_collatz_chain(n):
    collatz_chain = [n]
    cur = n
    while cur > 1:
        if cur % 2 == 0:
            cur = cur / 2
        else:
            cur = (3 * cur) + 1
        collatz_chain.append(int(cur))
    return collatz_chain

n_test_case = 13
n_question = 1_000_000

actual = solve(n_question)

print(f'{actual}\nNumber {actual[0]} has length: {len(actual)}')