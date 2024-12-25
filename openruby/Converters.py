def ascii_to_hex(text):
    return ''.join(format(ord(char), '02x') for char in text)

def hex_to_ascii(hex_string):
    return bytes.fromhex(hex_string).decode('utf-8')

def binary_to_text(binary):
    text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return text

def int_to_roman(n):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    for i in range(len(val)):
        count = n // val[i]
        roman_num += syb[i] * count
        n -= val[i] * count
    return roman_num

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_rankine(celsius: float) -> float:
    return celsius * 9/5 + 491.67

def celsius_to_newton(celsius):
    return celsius * 0.33

def celsius_to_romer(celsius):
    return (celsius * 21/40) + 7.5

def celsius_to_reaumur(celsius):
    return (celsius * 4/5)

def celsius_to_delisle(celsius):
    return (100 - celsius) * 3 / 2

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def fahrenheit_to_rankine(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius * 9/5 + 491.67

def fahrenheit_to_newton(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius * 0.33

def fahrenheit_to_romer(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return (celsius * 21/40) + 7.5

def fahrenheit_to_reaumur(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return (celsius * 4/5)

def fahrenheit_to_delisle(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return (100 - celsius) * 3 / 2

def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    return (celsius * 9/5) * 32

def kelvin_to_rankine(kelvin):
    celsius = kelvin - 273.15
    return celsius * 9/5 + 491.67

def kelvin_to_newton(kelvin):
    celsius = kelvin - 273.15
    return celsius * 0.33

def kelvin_to_romer(kelvin):
    celsius = kelvin - 273.15
    return (celsius * 21/40) + 7.5

def kelvin_to_reaumur(kelvin):
    celsius = kelvin - 273.15
    return (celsius * 4/5)

def kelvin_to_delisle(kelvin):
    celsius = kelvin - 273.15
    return (100 - celsius) * 3 / 2

def rankine_to_celsius(rankine):
    return (rankine - 491.67) * 5/9

def rankine_to_fahrenheit(rankine):
    return rankine - 459.67

def rankine_to_kelvin(rankine):
    return (rankine - 491.67) * 5/9 + 273.15

def rankine_to_newton(rankine):
    return (rankine - 491.67) * 5/9 * 33/100

def rankine_to_romer(rankine):
    return (rankine - 491.67) * 21/40 + 7.5

def rankine_to_reaumur(rankine):
    return (rankine - 491.67) * 4/5

def rankine_to_delisle(rankine):
    return (100 - (rankine - 491.67) * 9/5)

def newton_to_celsius(newton):
    return newton * (100 / 33)

def newton_to_fahrenheit(newton):
    return (newton * 60 / 11) + 32

def newton_to_kelvin(newton):
    return (newton * 100 / 33) + 273.15

def newton_to_rankine(newton):
    return (newton * 60 / 11) + 491.67

def newton_to_romer(newton):
    return (newton * 35 / 22) + 7.5

def newton_to_reaumur(newton):
    return newton * (80 / 33)

def newton_to_delisle(newton):
    return (33 - newton) * (50 / 11)

def romer_to_celsius(romer):
    return (romer - 7.5) * (40/21) + 273.15 - 273.15

def romer_to_fahrenheit(romer):
    return (romer - 7.5) * (40/21) * 1.8 + 32

def romer_to_kelvin(romer):
    return (romer - 7.5) * (40/21) + 273.15

def romer_to_rankine(romer):
    return (romer - 7.5) * (40/21) * 9/5 + 491.67

def romer_to_newton(romer):
    return (romer - 7.5) * (40/21) * 100/33 + 273.15

def romer_to_reaumur(romer):
    return (romer - 7.5) * (40/21) * 5/4 + 273.15

def romer_to_delisle(romer):
    return 373.15 - (romer - 7.5) * (40/21) * 2/3

def reaumur_to_celsius(reaumur):
    return (reaumur * 4) / 5

def reaumur_to_fahrenheit(reaumur):
    return (reaumur * 4 * 9/5) + 32

def reaumur_to_kelvin(reaumur):
    return (reaumur * 4) / 5 + 273.15

def reaumur_to_rankine(reaumur):
    return (reaumur * 4 * 9/5) + 491.67

def reaumur_to_newton(reaumur):
    return reaumur * 33/80

def reaumur_to_romer(reaumur):
    return (reaumur * 21/40) + 7.5

def reaumur_to_delisle(reaumur):
    return (373.15 - reaumur * 3/2)

def delisle_to_celsius(delisle):
    return 100 - (3/2) * delisle

def delisle_to_fahrenheit(delisle):
    return 212 - (6/5) * delisle

def delisle_to_kelvin(delisle):
    return 373.15 - (2/3) * delisle

def delisle_to_rankine(delisle):
    return 671.67 - (6/5) * delisle

def delisle_to_newton(delisle):
    return 33 - (11/50) * delisle

def delisle_to_romer(delisle):
    return 60 - (7/20) * delisle

def delisle_to_reaumur(delisle):
    return 80 - (8/15) * delisle

def number_to_words(n: int) -> str:
    if n < 0 or n > 9999:
        raise ValueError("Number must be between 0 and 9999.")

    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand"]

    def get_hundreds(num):
        result = ""
        if num >= 100:
            result += units[num // 100] + " Hundred"
            num %= 100
            if num > 0:
                result += " and "
        if 10 <= num < 20:
            result += teens[num - 10]
        else:
            if num >= 20:
                result += tens[num // 10]
                num %= 10
                if num > 0:
                    result += " "
            if num < 10 and num > 0:
                result += units[num]
        return result

    if n == 0:
        return "Zero"

    word = ""
    if n >= 1000:
        word += units[n // 1000] + " " + thousands[1]
        n %= 1000
        if n > 0:
            word += " "

    word += get_hundreds(n)
    return word

def time_to_words(hours: int, minutes: int) -> str:
    if not (0 <= hours < 24) or not (0 <= minutes < 60):
        raise ValueError("Hours must be between 0 and 23, and minutes between 0 and 59.")

    numbers = [
        "midnight", "one", "two", "three", "four", "five", "six", "seven", 
        "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", 
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", 
        "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five",
        "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine"
    ]
    
    if minutes == 0:
        if hours == 0 or hours == 12:
            return "midnight" if hours == 0 else "noon"
        return f"{numbers[hours % 12]} o'clock"

    if minutes == 15:
        return f"quarter past {numbers[hours % 12]}"

    if minutes == 30:
        return f"half past {numbers[hours % 12]}"

    if minutes == 45:
        return f"quarter to {numbers[(hours + 1) % 12]}"

    if minutes < 30:
        return f"{numbers[minutes]} past {numbers[hours % 12]}"

    return f"{numbers[60 - minutes]} to {numbers[(hours + 1) % 12]}"

def to_pig_latin(word: str) -> str:
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return word + "way"
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + "ay"
    return word
