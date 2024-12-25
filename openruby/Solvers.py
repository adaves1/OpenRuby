def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

def solve_n_queens(n):
    solutions = []
    solve_queen([], solutions, n)
    return solutions

def solve_queen(queens, solutions, n):
    row = len(queens)
    if row == n:
        solutions.append(queens)
        return

    for col in range(n):
        if all(abs(col - c) not in (0, row - r) for r, c in enumerate(queens)):
            solve_queen(queens + [col], solutions, n)

def dijkstra(graph, start):
    unvisited = {node: float('inf') for node in graph}
    unvisited[start] = 0
    visited = {}
    path = {}

    while unvisited:
        min_node = min(unvisited, key=unvisited.get)
        for neighbor, cost in graph[min_node].items():
            if neighbor in visited:
                continue
            new_cost = unvisited[min_node] + cost
            if new_cost < unvisited[neighbor]:
                unvisited[neighbor] = new_cost
                path[neighbor] = min_node
        visited[min_node] = unvisited[min_node]
        unvisited.pop(min_node)

    return visited, path

class Sudoku:

    def sudoku_solver(board):
        empty = Sudoku.find_empty(board)
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if Sudoku.is_valid(board, num, (row, col)):
                board[row][col] = num
                if Sudoku.sudoku_solver(board):
                    return True
                board[row][col] = 0

        return False

    def find_empty(board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(board, num, pos):
        for i in range(len(board[0])):
            if board[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False

        return True
    
class GameOfLife:

    def next_generation(board):
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        new_board = [[0] * len(board[0]) for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbors = sum(
                    board[i + dx][j + dy] == 1 for dx, dy in neighbors if 0 <= i + dx < len(board) and 0 <= j + dy < len(board[0])
                )
                if board[i][j] == 1 and live_neighbors in (2, 3):
                    new_board[i][j] = 1
                elif board[i][j] == 0 and live_neighbors == 3:
                    new_board[i][j] = 1

        return new_board    

    def game_of_life(board, generations):
        for _ in range(generations):
            board = GameOfLife.next_generation(board)
        return board

    
