def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
    
def monorocci(range, c):
    m = 2
    while m < range:
        c = m + 2
        m = c + 10
    print()

def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    a, b, c = 0, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
        return c

def tetranacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2 or n == 3:
        return 1
    a, b, c, d = 0, 1, 1, 1
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d
        return d
        

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def power_sum(n, exponent):
    return sum(i ** exponent for i in range(1, n + 1))

def is_kaprekar(n):
    squared_str = str(n * n)
    mid = len(squared_str) // 2
    left_part = int(squared_str[:mid] or "0")
    right_part = int(squared_str[mid:] or "0")
    return n == left_part + right_part

def nth_lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def nth_pell(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, 2 * b + a
    return a

def is_magic_square(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])
    
    for row in matrix:
        if sum(row) != magic_sum:
            return False

    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_sum:
            return False

    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False

    if sum(matrix[i][n - i - 1] for i in range(n)) != magic_sum:
        return False

    return True

def longest_common_subsequence(str1, str2):
    len1, len2 = len(str1), len(str2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = []
    i, j = len1, len2
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

def matrix_multiply(matrix_a, matrix_b):
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])

    if cols_a != rows_b:
        raise ValueError("Incompatible matrices for multiplication")

    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    result = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            result.append(i - 1)
            w -= weights[i - 1]

    result.reverse()
    return dp[n][capacity], result

def horner_polynomial(coeffs, x):
    result = 0
    for coeff in reversed(coeffs):
        result = result * x + coeff
    return result

def merge(left, right):
    sorted_arr = []
    while left and right:
        if left[0] <= right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))
    sorted_arr.extend(left or right)
    return sorted_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

def fastfouriertransform(x):
    N = len(x)
    if N <= 1:
        return x
    even = fastfouriertransform(x[0::2])
    odd = fastfouriertransform(x[1::2])
    combined = [0] * N
    for k in range(N // 2):
        t = complex(0, -2 * 3.141592653589793 * k / N) * odd[k]
        combined[k] = even[k] + t
        combined[k + N // 2] = even[k] - t
    return combined

def a_star(grid, start, end):
    open_set = {start}
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        current = min(open_set, key=lambda x: f_score.get(x, float('inf')))
        if current == end:
            return reconstruct_path(came_from, current)

        open_set.remove(current)
        for neighbor in get_neighbors(grid, current):
            tentative_g_score = g_score[current] + 1  
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                open_set.add(neighbor)

    return None

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def get_neighbors(grid, node):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = node[0] + dx, node[1] + dy
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
            neighbors.append((x, y))
    return neighbors

def newton_raphson(f, f_prime, x0, tolerance=1e-7, max_iterations=1000):
    x = x0
    for _ in range(max_iterations):
        fx = f(x)
        fpx = f_prime(x)
        if abs(fx) < tolerance:
            return x
        if fpx == 0:
            raise ValueError("Derivative is zero, cannot continue.")
        x = x - fx / fpx
    return x

def longest_increasing_subsequence(arr):
    if not arr:
        return []

    dp = [1] * len(arr)
    prev = [-1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    lis = []
    idx = max(range(len(dp)), key=dp.__getitem__)
    while idx != -1:
        lis.append(arr[idx])
        idx = prev[idx]

    return lis[::-1]

def geometric(n, a, r):
    return a * (r ** n)

def triangular(n):
    return n * (n + 1) // 2

def catalan(n):
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result = result * (2 * (2 * i - 1)) // (i + 1)
    return result

def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
