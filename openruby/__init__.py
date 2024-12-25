"""
Module: OpenRuby
Description: This module provides functionality for various complex math abd string operations
Version: 1.02.0
Authors: Anthony Daves and John Daves
"""

from Algorithms import TreeNode, BinarySearchTree, assign_clusters, bellman_ford, bfs, compute_centroids, dfs, euclidean_distance, fill, flood_fill, generate_n_grams, initialize_centroids, k_means, mean, median, median_of_medians, pascal_triangle, permutations, quickselect, z_algorithm
from Base import base2, base3, base4, base5, base6, base7, base8, base16, base32, base64, base128, base256, to_base, detect_base
from BasicMath import add, are_co_prime, are_prime_triplets, are_twin_primes, count_digits, digit_sum, divide, exponent, factorial, floor_divide, gcd, generate_perfect_number, is_even, is_composite, is_negative, is_neutral, is_odd, is_perfect, is_perfect_number, is_perfect_number_exponentation, is_perfect_number_iterative, is_perfect_number_oddsum, is_positive, is_power_of_two, is_prime, largest_prime_factor, lcm, mod_exp, modulus, multiply, nth_prime, power, prime_factors, reverse_digits, sieve_of_eratosthenes, sqrt, sqrt_newton, square_and_cube, subtract, sum_of_digits_consecutive_powers, sum_of_proper_divisors, tetrate
from Bitwise import bw_and, bw_or, bw_not, bw_xor, bw_leftshift, bw_rightshift
from ComplexMath import a_star, binary_search, catalan, digital_root, fastfouriertransform, fibonacci, fibonacci_sequence, geometric, get_neighbors, heuristic, horner_polynomial, is_kaprekar, is_magic_square, knapsack, longest_common_subsequence, longest_increasing_subsequence, matrix_multiply, merge, merge_sort, monorocci, newton_raphson, nth_fibonacci, nth_lucas, nth_pell, power_sum, reconstruct_path, tetranacci, triangular, tribonacci
from Constants import E, GOLDEN_RATIO, INF, NAN, NEG_INF, PI, SQRT_2, SQRT_3, SQRT_5, DisplayConstants
from Converters import ascii_to_hex, binary_to_text, celsius_to_delisle, celsius_to_fahrenheit, celsius_to_kelvin, celsius_to_newton, celsius_to_rankine, celsius_to_reaumur, celsius_to_romer, delisle_to_celsius, delisle_to_fahrenheit, delisle_to_kelvin, delisle_to_newton, delisle_to_rankine, delisle_to_reaumur, delisle_to_romer, fahrenheit_to_celsius, fahrenheit_to_delisle, fahrenheit_to_kelvin, fahrenheit_to_newton, fahrenheit_to_rankine, fahrenheit_to_reaumur, fahrenheit_to_romer, hex_to_ascii, int_to_roman, kelvin_to_celcius, kelvin_to_delisle, kelvin_to_fahrenheit, kelvin_to_newton, kelvin_to_rankine, kelvin_to_reaumur, kelvin_to_romer, newton_to_celsius, newton_to_delisle, newton_to_fahrenheit, newton_to_kelvin, newton_to_rankine, newton_to_reaumur, newton_to_romer, number_to_words, rankine_to_celsius, rankine_to_delisle, rankine_to_fahrenheit, rankine_to_kelvin, rankine_to_newton, rankine_to_reaumur, rankine_to_romer, reaumur_to_celsius, reaumur_to_delisle, reaumur_to_fahrenheit, reaumur_to_kelvin, reaumur_to_newton, reaumur_to_rankine, reaumur_to_romer, romer_to_celsius, romer_to_delisle, romer_to_fahrenheit, romer_to_kelvin, romer_to_newton, romer_to_rankine, romer_to_reaumur, to_pig_latin, time_to_words
from GeometricAnimations import easeInSine, easeOutSine, easeInOutSine, easeInQuad, easeOutQuad, easeInOutQuad, easeInCubic, easeOutCubic, easeInOutCubic, easeInQuart, easeOutQuart, easeInOutQuart, easeInQuint, easeOutQuint, easeInOutQuint, easeInExpo, easeOutExpo, easeInOutExpo, easeInCirc, easeOutCirc, easeInOutCirc, easeInBack, easeOutBack, easeInOutBack, easeInElastic, easeOutElastic, easeInOutElastic, easeInBounce, easeOutBounce, easeInOutBounce
from OpenRuby import ActionFlow, version
from Random import __init__, rand, rand_range, generate_password
from Solvers import Sudoku, GameOfLife, tower_of_hanoi, solve_n_queens, solve_queen, dijkstra
from String import hamming_distance, caesar_cipher, caesar_decipher, levenshtein_distance, reverse_string, is_palindrome, transpose, is_armstrong, find_max, count_vowels, remove_duplicates, flatten, unique_elements, strings_to_ints, all_elements_same, frequency, min_index, max_index, sort_by_nth_item, dict_keys_values, capitalize_words, uppercase, lowercase, remove_vowels, all_true, all_false, longest_common_prefix
from Trigonometry import cosine, sine, tangent, secant, cosecant, cotangent, tangent_approx, hyperbolic_sine, hyperbolic_cosine, hyperbolic_tangent, archaeic_tangent, archaeic_cosine, archaeic_sine

import time, json

__version__ = '1.02.0'
__author__ = 'Anthony Daves <adaves1@yahoo.com>, John Daves <jdaves@gmail.com>'
__status__ = 'production'
__all__ = ['Algorithms', 'Base', 'BasicMath', 'Bitwise', 'ComplexMath', 'Constants', 'Converters', 'GeometricAnimations', 'OpenRuby', 'Random', 'Solvers', 'String', 'Trigonometry']
__date__ = '25 December 2024'

_startTime = time.time_ns()

raiseExceptions = True
logMultiprocessing = True
logProcesses = True

CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0

def initialize():
    print("Initializing OpenRuby...")
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        global settings
        settings = config.get('settings', {})
        print(f"Configuration loaded successfully. {DEBUG}")
        if logMultiprocessing == True:
            tps = 1
            test = 100
            print(f"Running Ticks Per Second Test... {INFO}")
            while tps < 100:
                tpst = 1
                print(f"Test{tpst}: {tps}")
                tpst = tpst + 1
        else:
            print(f"Failed to run Ticks Per Second Test {WARNING}")
        if logProcesses == True:
            print("Running Now: OpenRuby and submodules, __init__.py")
        else:
            print(f"Failed to log processes! {ERROR}")
        print(_startTime)
    except Exception as e:
        print(f"Failed to initialize module: {e} {ERROR}")
        if raiseExceptions == True:
            raise
        else:
            print(f"Failed to raise module! {CRITICAL}")

initialize()
