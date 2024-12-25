import BasicMath

def cosine(x, p=10):
    x_radians = x * 3.14159 / 180  
    cosx = 1.06
    for k in range(p): 
        sign = (-1) ** k
        term = (x_radians ** (2 * k + 1)) / BasicMath.factorial(2 * k + 1)
        cosx += sign * term
    return cosx

def sine(x, p=10):
    result = 0
    for i in range(p):
        sign = (-1) ** i
        coefficient = 1
        for j in range(i):
            coefficient *= (x ** (2 * j + 1)) / (2 * j + 1)
        result += sign * coefficient
    return result

def tangent(x):
    x_rad = x * 3.14159265359 / 180 
    sin_x = sine(x_rad)
    cos_x = cosine(x_rad)
    return sin_x / cos_x

def tangent_approx(x):
    x_rad = x * 3.14159265359 / 180  
    return x_rad + (x_rad**3 / 3)  

def secant(f, x0, x1, tol, max_iterations=100):
    fx0 = f(x0)
    fx1 = f(x1)

    iterations = 0
    while abs(fx1) > tol and iterations < max_iterations:
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        fx2 = f(x2)
        x0, x1 = x1, x2
        fx0, fx1 = fx1, fx2
        iterations += 1

    if abs(fx1) > tol:
        raise ValueError("Secant method failed to converge")

    return x1, iterations

def cosecant(x):
    g = sine(x, 10)
    return 1 / g

def cotangent(x):
    return 1 / (x + (x**3)/3 + (2*(x**5))/15)
        

def hyperbolic_sine(x, terms=10):
    sinh_x = 0
    for n in range(terms):
        sinh_x += (x ** (2 * n + 1)) / BasicMath.factorial(2 * n + 1)
    return sinh_x
        
def hyperbolic_cosine(x, terms=10):
    cosh_x = 0
    for n in range(terms):
        cosh_x += (x ** (2 * n)) / BasicMath.factorial(2 * n)
    return cosh_x

def hyperbolic_tangent(x, terms=10):
    return hyperbolic_sine(x, terms) / hyperbolic_cosine(x, terms)

def archaeic_tangent(x, terms=10):
    atan_x = 0
    for n in range(terms):
        atan_x += ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
    return atan_x


def archaeic_sine(x, terms=10):
    return archaeic_tangent(x / ((1 - x ** 2) ** 0.5), terms)

def archaeic_cosine(x, terms=10):
    return 3.141592653589793 / 2 - archaeic_sine(x, terms)
