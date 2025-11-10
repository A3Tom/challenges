# Lexicographic Permutations

# [0, 1, 2]
#  x

def solve(digits: list = []):
    return backtrack(digits)
    

def backtrack(available: list, current: list = [], res: list = []):
    if len(current) == len(available):
        res.append(current.copy())
        if len(res) == 1_000_000:
            print(f'1_000_000th perm: {current}')
        return
    
    for i in range(0, len(available)):
        choice = available[i]
        if not current.__contains__(choice):
            current.append(choice)
            backtrack(available, current, res)
            current.pop()
    
    return res


n_test_case=[0, 1, 2, 3]
n_question=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

actual = solve(n_question)
# print(actual)