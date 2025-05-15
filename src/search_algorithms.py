import random
import time
from collections import deque
import heapq
import math

# Directions (Up, Down, Left, Right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Random movement algorithm (limited moves)
def random_move(start, goal, obstacles, rows, cols):
    start_time = time.time()
    path = []
    current = start

    for _ in range(1000):  # Limit to 1000 moves
        direction = random.choice(DIRECTIONS)
        new_pos = (current[0] + direction[0], current[1] + direction[1])

        if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and new_pos not in obstacles:
            path.append(direction)
            current = new_pos

        if current == goal:
            print(f"Random Move Time Taken: {time.time() - start_time:.7f} seconds")
            return path

    print(f"Random Move Time Taken: {time.time() - start_time:.7f} seconds")
    return []  # If it takes too long, return empty path

# Breadth First Search (BFS)
def bfs(start, goal, obstacles, rows, cols):
    start_time = time.time()
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()
        
        if current == goal:
            print(f"BFS Time Taken: {time.time() - start_time:.7f} seconds")
            return path

        for direction in DIRECTIONS:
            new_pos = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and new_pos not in obstacles and new_pos not in visited:
                visited.add(new_pos)
                queue.append((new_pos, path + [direction]))

    print(f"BFS Time Taken: {time.time() - start_time:.7f} seconds")
    return []

# Depth First Search (DFS)
def dfs(start, goal, obstacles, rows, cols):
    start_time = time.time()

    stack = [(start, [])]
    visited = set([start])

    while stack:
        current, path = stack.pop()
        
        if current == goal:
        
            print(f"DFS Time Taken: {time.time() - start_time:.7f} seconds")
            #print(f"DFS Time Taken: {time.time() - start_time} seconds")
            #print(f"DFS Time Taken: {int(time.time() - start_time)} seconds")
            
      



            return path

        for direction in DIRECTIONS:
            new_pos = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and new_pos not in obstacles and new_pos not in visited:
                visited.add(new_pos)
                stack.append((new_pos, path + [direction]))

    print(f"DFS Time Taken: {time.time() - start_time:.7f} seconds")
    return []

# Iterative Deepening Search (IDS)
def ids(start, goal, obstacles, rows, cols):
    start_time = time.time()
    time_limit = 5  # Time limit in seconds

    def dls(node, depth, visited):
        if node == goal:
            return []
        if depth == 0:
            return None
        if time.time() - start_time > time_limit:  # Check if time exceeded
            return "Time Limit Exceeded"

        visited.add(node)
        for direction in DIRECTIONS:
            new_pos = (node[0] + direction[0], node[1] + direction[1])
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and new_pos not in obstacles and new_pos not in visited:
                result = dls(new_pos, depth - 1, visited)
                if result == "Time Limit Exceeded":
                    return result
                if result is not None:
                    return [direction] + result
        return None

    depth = 0
    while True:
        visited = set()
        result = dls(start, depth, visited)
        if result == "Time Limit Exceeded":
            print(f"IDS Time Limit Exceeded. Score: {len(visited)}")
            return []
        if result is not None:
            print(f"IDS Time Taken: {time.time() - start_time:.7f} seconds")
            return result
        depth += 1

# Uniform Cost Search (UCS)
def ucs(start, goal, obstacles, rows, cols):
    start_time = time.time()
    pq = [(0, start, [])]
    visited = set()
    cost_so_far = {start: 0}

    while pq:
        cost, current, path = heapq.heappop(pq)
        
        if current == goal:
            print(f"UCS Time Taken: {time.time() - start_time:.7f} seconds")
            return path
        
        if current in visited:
            continue
        visited.add(current)

        for direction in DIRECTIONS:
            new_pos = (current[0] + direction[0], current[1] + direction[1])
            new_cost = cost + 1

            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and new_pos not in obstacles:
                if new_pos not in cost_so_far or new_cost < cost_so_far[new_pos]:
                    cost_so_far[new_pos] = new_cost
                    heapq.heappush(pq, (new_cost, new_pos, path + [direction]))

    print(f"UCS Time Taken: {time.time() - start_time:.7f} seconds")
    return []

# Greedy Best First Search
def greedy_bfs(start, goal, obstacles, rows, cols):
    start_time = time.time()
    heuristic = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

    pq = [(heuristic(start, goal), start, [])]
    visited = set([start])

    while pq:
        _, current, path = heapq.heappop(pq)
        
        if current == goal:
            print(f"Greedy BFS Time Taken: {time.time() - start_time:.7f} seconds")
            return path

        for direction in DIRECTIONS:
            new_pos = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and new_pos not in obstacles and new_pos not in visited:
                visited.add(new_pos)
                heapq.heappush(pq, (heuristic(new_pos, goal), new_pos, path + [direction]))

    print(f"Greedy BFS Time Taken: {time.time() - start_time:.7f} seconds")
    return []

# A* Search
def astar(start, goal, obstacles, rows, cols):
    start_time = time.time()
    heuristic = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

    pq = [(heuristic(start, goal), 0, start, [])]
    visited = set()
    cost_so_far = {start: 0}

    while pq:
        _, cost, current, path = heapq.heappop(pq)

        if current == goal:
            #print(f"A* Time Taken: {time.time() - start_time:.7f} seconds")
            print(f"A* Time Taken: {time.time() - start_time} seconds")

            return path
        
        if current in visited:
            continue
        visited.add(current)

        for direction in DIRECTIONS:
            new_pos = (current[0] + direction[0], current[1] + direction[1])
            new_cost = cost + 1

            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and new_pos not in obstacles:
                if new_pos not in cost_so_far or new_cost < cost_so_far[new_pos]:
                    cost_so_far[new_pos] = new_cost
                    priority = new_cost + heuristic(new_pos, goal)
                    heapq.heappush(pq, (priority, new_cost, new_pos, path + [direction]))

    print(f"A* Time Taken: {time.time() - start_time:.7f} seconds")
    return []