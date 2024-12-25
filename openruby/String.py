def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")
    return sum(el1 != el2 for el1, el2 in zip(str1, str2))

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + shift - offset) % 26 + offset)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

def levenshtein_distance(str1, str2):
    dp = [[i + j if i * j == 0 else 0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + (str1[i-1] != str2[j-1]))
    return dp[-1][-1]

def reverse_string(text):
    return text[::-1]
    
def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

def transpose(matrix):
    return list(map(list, zip(*matrix)))

def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    return n == sum(int(digit) ** num_digits for digit in num_str)

def find_max(lst):
    return max(lst) if lst else None

def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def remove_duplicates(lst):
    return list(set(lst))

def flatten(lst):
    return [item for sublist in lst for item in sublist]

def unique_elements(lst):
    return list(dict.fromkeys(lst))

def strings_to_ints(lst):
    return [int(x) for x in lst]

def all_elements_same(lst):
    return len(set(lst)) == 1
    
def frequency(lst):
    freq_dict = {}
    for item in lst:
        freq_dict[item] = freq_dict.get(item, 0) + 1
    return freq_dict

def min_index(lst):
    return lst.index(min(lst))

def max_index(lst):
    return lst.index(max(lst))

def sort_by_nth_item(lst, n):
    return sorted(lst, key=lambda x: x[n])

def dict_keys_values(d):
    return list(d.keys()), list(d.values())

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def uppercase(s):
    return s.upper()

def lowercase(s):
    return s.lower()
    
def remove_vowels(s):
    return ''.join(c for c in s if c.lower() not in 'aeiou')

def all_true(lst):
    return all(lst)

def all_false(lst):
    return not any(lst)

def longest_common_prefix(str1: str, str2: str) -> str:
    prefix = ""
    min_length = min(len(str1), len(str2))

    for i in range(min_length):
        if str1[i] == str2[i]:
            prefix += str1[i]
        else:
            break

    return prefix
