import Trigonometry
import BasicMath

def easeInSine(x: int):
    return 1 - Trigonometry.cosine((x * 3.141592653589793) / 2)

def easeOutSine(x: int):
    return Trigonometry.sine((x * 3.141592653589793) / 2)
    
def easeInOutSine(x: int):
    return -(Trigonometry.cosine(3.141592653589793 * x) - 1) / 2
    
def easeInQuad(x: int):
    return x * x
    
def easeOutQuad(x: int):
    return 1 - (1 - x) * (1 - x)
    
def easeInOutQuad(x: int):
    return 2 * x * x if x < 0.5 else 1 - BasicMath.exponent(-2 * x + 2, 2) / 2
    
def easeInCubic(x: int):
    return x * x * x
    
def easeOutCubic(x: int):
    return 1 - BasicMath.exponent(1 - x, 3)
    
def easeInOutCubic(x: int):
    return 4 * x * x * x if x < 0.5 else 1 - BasicMath.exponent(-2 * x + 2, 3) / 2
    
def easeInQuart(x: int):
    return x * x * x * x 
    
def easeOutQuart(x: int):
    return 1 - BasicMath.exponent(1 - x, 4)
    
def easeInOutQuart(x: int):
    return 8 * x * x * x * x if x < 0.5 else 1 - BasicMath.exponent(-2 * x + 2, 4) / 2
    
def easeInQuint(x: int):
    return x * x * x * x * x 
    
def easeOutQuint(x: int):
    return 1 - BasicMath.exponent(1 - x, 5)
    
def easeInOutQuint(x: int):
    return 16 * x * x * x * x * x if x < 0.5 else 1 - BasicMath.exponent(-2 * x + 2, 5) / 2
    
def easeInExpo(x: int):
    return 0 if x == 0 else BasicMath.exponent(2, 10 * x - 10)
 
def easeOutExpo(x: int):
    return 1 if x == 1 else 1 - BasicMath.exponent(2, -10 * x)

def easeInOutExpo(x: int):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x < 0.5:
        return BasicMath.exponent(2, 20 * x - 10) / 2
    else:
        return (2 - BasicMath.exponent(2, -20 * x + 10)) / 2

def easeInCirc(x: int):
    return 1 - BasicMath.sqrt(1 - BasicMath.exponent(x, 2))
    
def easeOutCirc(x: int):
    return BasicMath.sqrt(1 - BasicMath.exponent(x - 1, 2))
    
def easeInOutCirc(x: int):
    return (1 - BasicMath.sqrt(1 - BasicMath.exponent(2 * x, 2))) / 2 if x < 0.5 else (BasicMath.sqrt(1 - BasicMath.exponent(-2 * x + 2, 2)) + 1) / 2

def easeInBack(x: int):
    c1 = 1.70158
    c3 = c1 + 1
    return c3 * x * x * x - c1 * x * x

def easeOutBack(x: int):
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * BasicMath.exponent(x - 1, 3) + c1 * BasicMath.exponent(x - 1, 2)

def easeInOutBack(x: int):
    c1 = 1.70158
    c2 = c1 * 1.525
    return (BasicMath.exponent(2 * x, 2) * ((c2 + 1) * 2 * x - c2)) / 2 if x < 0.5 else (BasicMath.exponent(2 * x - 2, 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2

def easeInElastic(x: int):
    c4 = (2 * 3.141592653589793) / 3
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return -(BasicMath.exponent(2, 10 * x - 10) * Trigonometry.sine((x * 10 - 10.75) * c4))

def easeOutElastic(x: int):
    c4 = (2 * 3.141592653589793) / 3
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return BasicMath.exponent(2, -10 * x) * Trigonometry.sine((x * 10 - 0.75) * c4) + 1

def easeInOutElastic(x: int):
    c5 = (2 * 3.141592653589793) / 4.5
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x < 0.5:
        return -(BasicMath.exponent(2, 20 * x - 10) * Trigonometry.sine((20 * x - 11.125) * c5)) / 2
    else:
        return (BasicMath.exponent(2, -20 * x + 10) * Trigonometry.sine((20 * x - 11.125) * c5)) / 2 + 1

def easeOutBounce(x: int):
    n1 = 7.5625
    d1 = 2.75
    if x < 1 / d1:
        return n1 * x * x
    elif x < 2 / d1:
        x -= 1.5 / d1
        return n1 * x * x + 0.75
    elif x < 2.5 / d1:
        x -= 2.25 / d1
        return n1 * x * x + 0.9375
    else:
        x -= 2.625 / d1
        return n1 * x * x + 0.984375

def easeInBounce(x: int):
    return 1 - easeOutBounce(1 - x)

def easeInOutBounce(x: int):
    return (1 - easeOutBounce(1 - 2 * x)) / 2 if x < 0.5 else (1 + easeOutBounce(2 * x - 1)) / 2
