def exponent(x, y):
    return x ** y

def tetrate(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    return base ** tetrate(base, exponent - 1)
    
def power(n):
    return n * n
    
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
    
def sqrt(x, tolerance=1e-6):
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")

    guess = x / 2.0
    while True:
        better_guess = 0.5 * (guess + x / guess)
        if abs(guess - better_guess) < tolerance:
            return better_guess
        guess = better_guess
        
def sqrt_newton(x, tolerance=1e-6):
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")

    guess = x / 2.0
    while True:
        better_guess = 0.5 * (guess + x / guess)
        if abs(guess - better_guess) < tolerance:
            return better_guess
        guess = better_guess
        
def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y
    
def multiply(x, y):
    return x * y
    
def divide(x, y):
    return x / y
    
def modulus(x, y):
    return x % y

def floor_divide(x, y):
    return x // y
    

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return abs(x * y) // gcd(x, y) if x and y else 0

def mod_exp(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if (exponent % 2) == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nth_prime(n):
    count = 0
    candidate = 2
    while count < n:
        if is_prime(candidate):
            count += 1
        candidate += 1
    return candidate - 1

def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def is_even(n):
    if n % 2 == 0:
        return True
    else:  
        return False
    
def is_odd(n):
    if n % 2 != 0:
        return True
    else:  
        return False
    
def is_composite(n):
    if n < 4:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

def is_neutral(n):
    if n == 0:
        return True
    elif n == 1:
        return True
    else:
        return False
    
def is_positive(n):
    if n > 0:
        return True
    else:
        return False
    
def is_negative(n):
    if n < 0:
        return True
    else:
        return False
    
def are_twin_primes(a, b):
    if abs(a - b) == 2:
        if is_prime(a) and is_prime(b):
            return True
    return False

def are_prime_triplets(a, b, c):
    if abs(a - b) == 2 and abs(b - c) == 2:
        if is_prime(a) and is_prime(b) and is_prime(c):
            return True
    return False

def are_co_prime(a: int, b: int):
    if gcd(a, b) == 1:
        return True
    else:
        return False
    
def is_perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def is_perfect_number_iterative(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def is_perfect_number_exponentation(n):
    guess = n // 2
    guess_squared = guess ** 2
    while guess_squared != n:
        guess = (guess + n // guess) // 2
        guess_squared = guess ** 2
    return guess_squared == n

def is_perfect_number_oddsum(n):
    sum = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            sum += i
            if i * i != n:
                sum += n // i
        i += 2
    return sum == n

def generate_perfect_number(n):
    if n < 1:
        return "The Number cannot be less than 1."
    else:
        return n * n 
        
def sum_of_proper_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

def square_and_cube(n):
    return n ** 2, n ** 3

def count_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

def sum_of_digits_consecutive_powers(n):
    return sum(int(digit) ** (index + 1) for index, digit in enumerate(str(n)))

def largest_prime_factor(n):
    factor = 2
    last_factor = 1
    while n > 1:
        if n % factor == 0:
            last_factor = factor
            n //= factor
            while n % factor == 0:
                n //= factor
        factor += 1
    return last_factor

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def reverse_digits(n):
    reversed_number = 0
    while n > 0:
        reversed_number = reversed_number * 10 + n % 10
        n //= 10
    return reversed_number

def is_perfect(n):
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
