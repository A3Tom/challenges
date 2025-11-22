# Reciprocal Cycles
from decimal import *

DECIMAL_PRECISION = 302
getcontext().prec = DECIMAL_PRECISION


# 11111111111111111111 1
# 12121212121212121212 2
# 12312312312312312312 -
# 12341234123412341234 4
# 12345123451234512345 5
# str = '12345123451234512345'
# 1234512345 | 1234512345
# 12345 | 12345 | 12345 | 12345
# 123451234512345
# 1234512345
# 12345
# 23451234512345
# 234512345
# 2345
# 3451234512345
# 34512345
# 345
# 451234512345
# 4512345
# 45
# 51234512345
# 512345
# 5



def solve(n):
    max_reciprocal_cycle = build_cycle_vm(0, '', 0)

    for i in range(1, n, 2):
        dec = Decimal(1) / Decimal(i)
        cycle = compute_reciprocal_cycle(str(dec)[2:])
        
        if len(cycle) > len(max_reciprocal_cycle['pattern']):
            max_reciprocal_cycle = build_cycle_vm(i, cycle, dec)

    return max_reciprocal_cycle
    
def build_cycle_vm(n: int, pattern: str, result: Decimal):
    return {
        'number': n,
        'pattern': pattern,
        'result': str(result)
    }

def compute_reciprocal_cycle(s: str):
    suffixes = []

    i = 0
    while i < len(s):
        suffixes.append(s[i:])
        i += 1

    suffixes.sort()
    lcp = compute_lcp(suffixes)
    tiling_pattern = get_tiling_pattern(lcp)
    return tiling_pattern


def compute_lcp(suffixes: list = []):
    suffixes.sort()
    lcp = ''

    i = 1
    while i < len(suffixes):
        s1 = suffixes[i]
        s2 = suffixes[i - 1]

        prefix = get_common_prefix(s1, s2)
        if len(prefix) > len(lcp):
            lcp = prefix 
        i += 1
    
    return lcp

def get_common_prefix(s1, s2):
    prefix = ''
    commonality = 0
    j = 0
    while s1[commonality] == s2[j]:
        prefix += s1[commonality]

        commonality += 1
        j += 1

        if commonality == len(s1):
            break

        if j > len(s2) - 1:
            j = 0

    return prefix

def get_tiling_pattern(s: str):
    i = 0
    border = ''
    while i < len(s):
        prefix = s[0:i]
        suffix = s[len(s)-i:len(s)]

        if prefix == suffix and len(prefix) > len(border):
            border = prefix
        i+= 1

    return s[:-len(border)]

n_test_case = 11
n_question = 1000
actual = solve(n_question)
# actual = compute_reciprocal_cycle(str(Decimal(1) / Decimal(983)))

print(
    f"""
    Number: {actual['number']}
    Pattern: ({len(actual['pattern'])}) {actual['pattern']}
    Result: {actual['result']}
    """
)

# 0.004975124378109452736318407960199004975124378109452736318407960199004975124378109452736318407960199