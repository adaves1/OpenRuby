def base2(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

def base3(text):
    base3_digits = '012'
    result = ''
    for char in text:
        char_code = ord(char)
        base3_val = ''
        while char_code > 0:
            base3_val = base3_digits[char_code % 3] + base3_val
            char_code //= 3
        result += base3_val + ' '
    return result.strip()

def base4(n):
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        n, remainder = divmod(n, 4)
        result = str(remainder) + result
    return result

def base5(n):
    if n == 0:
        return '0'
    digits = []
    while n > 0:
        digits.append(str(n % 5))
        n //= 5
    return ''.join(reversed(digits))

def base6(text):
    base6_digits = '012345'
    result = ''
    for char in text:
        ascii_val = ord(char)
        base6_val = ''
        while ascii_val > 0:
            base6_val = base6_digits[ascii_val % 6] + base6_val
            ascii_val //= 6
        result += base6_val
    return result

def base7(n):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        n, remainder = divmod(n, 7)
        result = str(remainder) + result
    return result

def base8(n):
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        result = str(n % 8) + result
        n //= 8
    return result

def base16(n):
    hex_result = ""
    while n > 0:
        n, remainder = divmod(n, 16)
        hex_result = hex(remainder).lstrip("0") or "0" + hex_result
    return hex_result

def base32(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    result = ""

    for byte in text.encode():
        result += alphabet[byte >> 5]
        result += alphabet[byte & 0x1f]

    return result

def base64(text):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binary_to_base64 = {
        "000000": "A", "000001": "B", "000010": "C", "000011": "D", "000100": "E", "000101": "F",
        "000110": "G", "000111": "H", "001000": "I", "001001": "J", "001010": "K", "001011": "L",
        "001100": "M", "001101": "N", "001110": "O", "001111": "P", "010000": "Q", "010001": "R",
        "010010": "S", "010011": "T", "010100": "U", "010101": "V", "010110": "W", "010111": "X",
        "011000": "Y", "011001": "Z", "011010": "2", "011011": "3", "011100": "4", "011101": "5",
        "011110": "6", "011111": "7", "100000": "8", "100001": "9", "100010": "+", "100011": "/",
        "100100": "=", "100101": "", "100110": "", "100111": "", "101000": "", "101001": "",
        "101010": "", "101011": "", "101100": "", "101101": "", "101110": "", "101111": "",
        "110000": "", "110001": "", "110010": "", "110011": "", "110100": "", "110101": "",
        "110110": "", "110111": "", "111000": "", "111001": "", "111010": "", "111011": "",
        "111100": "", "111101": "", "111110": "", "111111": ""
    }

    base64_text = ""
    for char in text:
        binary = format(ord(char), "06b")
        base64_text += binary_to_base64.get(binary, "")

    return base64_text

def base128(text):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    result = ""
    for char in text:
        ascii_val = ord(char)
        base128_val = ""
        while ascii_val > 0:
            base128_val = chars[ascii_val % 128] + base128_val
            ascii_val //= 128
        result += base128_val
    return result

def base256(text):
    binary = ""
    for char in text:
        byte = ord(char)
        binary += format(byte, '08b')
    return hex(int(binary, 2))

def to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(str(n % base))
        n //= base
    return ''.join(digits[::-1])

def detect_base(number):
    if all(c in '01' for c in number):
        return "Binary (Base 2)"
    elif all(c in '01234567' for c in number):
        return "Octal (Base 8)"
    elif all(c in '0123456789' for c in number):
        return "Decimal (Base 10)"
    elif all(c in '0123456789abcdefABCDEF' for c in number):
        return "Hexadecimal (Base 16)"
    else:
        return "Base cannot be detected by our systems. Please inform at adaves1@yahoo.com . ERR-BU"