import math

MAX_INTEGER = 28124

def solve():
    abundant_numbers = get_abundant_numbers()
    sum_perms = get_two_sum_permutations(abundant_numbers)
    inverse_sum_perms = invert_integer_array(sum_perms, MAX_INTEGER)
    return [inverse_sum_perms[-1], sum_perms[-1], abundant_numbers[-1], sum(inverse_sum_perms)]

def invert_integer_array(arr = [], max_int = 1):
    unique_arr = dict.fromkeys(arr)
    return [i for i in range(0, max_int) if unique_arr.get(i, True)]

def get_two_sum_permutations(arr = []):
    if len(arr) < 2:
        return []
    
    sum_permutation_arr = []
    i = 0
    j = 0

    while i < len(arr) - 1:
        if i > MAX_INTEGER:
            break

        while j < len(arr):
            sum_result = arr[i] + arr[j]
            
            if(sum_result > MAX_INTEGER): 
                break

            sum_permutation_arr.append(sum_result)
            j += 1
        i += 1
        j = i
        
    return sum_permutation_arr
        
def get_abundant_numbers():
    i = 12
    abundant_numbers = []

    while i < MAX_INTEGER:
        proper_factors = get_proper_factors(i)
        if is_abundant_number(i, proper_factors):
            abundant_numbers.append(i)
        i += 1

    return abundant_numbers

def get_proper_factors(n):
    divisor_l = []

    median_divisor = math.floor(math.sqrt(n))
    for i in range(1, median_divisor + 1):
        div_result = n / i

        if (div_result).is_integer():
            if div_result != n:
                divisor_l.append(int(div_result))

            if i != int(div_result):
                divisor_l.append(i)

    return divisor_l

def is_abundant_number(n, proper_factors):
    return sum(proper_factors) > n

actual = solve()
print(actual)