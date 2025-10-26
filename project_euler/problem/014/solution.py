# Longest Collatz Sequence

# The following iterative sequence is defined for the set of positive integers:
#     n -> n/2 (n is even)
#     n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence: 
#     13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

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