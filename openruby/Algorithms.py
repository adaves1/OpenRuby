def assign_clusters(data, centroids):
    clusters = [[] for _ in centroids]
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        closest_index = distances.index(min(distances))
        clusters[closest_index].append(point)
    return clusters

def bellman_ford(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distance[node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[node] + weight
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distance[node] + weight < distance[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distance

def bfs(graph, start):
    visited = set()
    queue = [start]
    result = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return result

def compute_centroids(data, clusters, k):
    centroids = []
    for i in range(k):
        if clusters[i]:  
            centroids.append([sum(dim) / len(clusters[i]) for dim in zip(*clusters[i])])
        else:
            centroids.append([0] * len(data[0]))  
    return centroids

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

def euclidean_distance(point1, point2):
    return sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)) ** 0.5

def fill(image, x, y, old_color, new_color):
    if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != old_color:
        return

    image[x][y] = new_color
    fill(image, x + 1, y, old_color, new_color)
    fill(image, x - 1, y, old_color, new_color)
    fill(image, x, y + 1, old_color, new_color)
    fill(image, x, y - 1, old_color, new_color)

def flood_fill(image, x, y, new_color):
    old_color = image[x][y]
    if old_color == new_color:
        return

    fill(image, x, y, old_color, new_color)

def generate_n_grams(text, n):
    words = text.split()
    n_grams = []
    for i in range(len(words) - n + 1):
        n_grams.append(tuple(words[i:i + n]))
    return n_grams

def initialize_centroids(data, k):
    return data[:k]  

def k_means(data, k, max_iterations=100):
    centroids = initialize_centroids(data, k)
    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = compute_centroids(data, clusters, k)
        if centroids == new_centroids:
            break
        centroids = new_centroids
    return clusters, centroids

def mean(data):
    return sum(data) / len(data)

def median(data):
    sorted_data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]

def median_of_medians(lst, k):
    if len(lst) <= 5:
        return sorted(lst)[k]

    sublists = [lst[i:i + 5] for i in range(0, len(lst), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    pivot = median_of_medians(medians, len(medians) // 2)

    low = [x for x in lst if x < pivot]
    high = [x for x in lst if x > pivot]
    pivot_count = lst.count(pivot)

    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + pivot_count:
        return pivot
    else:
        return median_of_medians(high, k - len(low) - pivot_count)

def pascal_triangle(rows):
    triangle = []
    for row in range(rows):
        new_row = [1]
        if triangle:
            last_row = triangle[-1]
            new_row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            new_row.append(1)
        triangle.append(new_row)
    return triangle

def permutations(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in permutations(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

def z_algorithm(s):
    z = [0] * len(s)
    l, r, k = 0, 0, 0
    for i in range(1, len(s)):
        if i > r:
            l, r = i, i
            while r < len(s) and s[r] == s[r - l]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < len(s) and s[r] == s[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def find(self, key):
        return self._find_rec(self.root, key)

    def _find_rec(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._find_rec(node.left, key)
        return self._find_rec(node.right, key)
