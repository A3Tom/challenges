import math

MAX_VALUE: int = 1000

class QuadraticConfiguration:
    def __init__(self, n: int, co_a: int, co_b: int, quad_result: int = 0):
        self.n = n
        self.co_a = co_a
        self.co_b = co_b
        self.quad_result = quad_result
        
def solve():
    possible_co_b = get_primes(MAX_VALUE)
    max_config = QuadraticConfiguration(0, 0, 0, 0)

    for co_b in possible_co_b:
        config = get_conseq_quad_configs(co_b)
        if config.n > max_config.n:
            max_config = config

        config = get_conseq_quad_configs(-co_b)
        if config.n > max_config.n:
            max_config = config

    return max_config

def get_conseq_quad_configs(co_b: int) -> QuadraticConfiguration:
    max_config = QuadraticConfiguration(0, 0, 0, 0)
    
    for co_a in range(-MAX_VALUE, MAX_VALUE):
        n = 0
        while True:
            quad_result = quadratic_formula(n, co_a, co_b)
            if not is_prime(abs(quad_result)):
                if n > max_config.n:
                    max_config = QuadraticConfiguration(n, co_a, co_b, quad_result)
                break
            n += 1

    return max_config

def quadratic_formula(n:int, a: int, b: int):
    return int(math.pow(n, 2) + (a * n) + b)

def get_primes(n):
    return [i for i in range(2, n) if is_prime(i)]

def is_prime(n):
    half_n = (n//2) + 1
    for i in range(2, half_n):
        if i > 2 and i % 2 == 0:
            continue
        if n % i == 0:
            return False
    return True

actual = solve()
print(f"""
a = {actual.co_a}
b = {actual.co_b}
n = {actual.n}
product = {actual.co_a * actual.co_b}
""")