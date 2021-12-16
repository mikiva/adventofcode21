import heapq
from collections import defaultdict

right = (0, 1)
left = (0, -1)
down = (1, 0)
up = (-1, 0)


def get_neighbors(graph, c):
    neighbors = []
    for d in [up, down, left, right]:
        nc = tuple(map(lambda i, j: i + j, c, d))
        if nc in graph:
            neighbors.append(nc)
    return neighbors


def take_a_walk(graph, start, end):
    path = []
    heapq.heappush(path, (0, start))
    current_risk = defaultdict(int)
    current_risk[start] = 0
    while path:
        c = heapq.heappop(path)[1]
        if c == end:
            break

        for neighbor in get_neighbors(graph, c):
            nr = current_risk[c] + graph[neighbor]
            if neighbor not in current_risk or nr < current_risk[neighbor]:
                current_risk[neighbor] = nr
                prio = nr
                heapq.heappush(path, (prio, neighbor))

    return current_risk[end]


def expand_map(small):
    y, x = len(small), len(small[0])
    big = [[0] * (5 * x) for _ in range(5 * y)]
    for row in range(5):
        for col in range(5):
            for r in range(y):
                for c in range(x):
                    nr, nc = y * row + r, x * col + c
                    big[nr][nc] = small[r][c] + row + col
                    if big[nr][nc] > 9:
                        big[nr][nc] -= 9

    return big


def build_graph(lines):
    graph = defaultdict(int)
    for y, line in enumerate(lines):
        for x, cost in enumerate(line):
            graph[(x, y)] = int(cost)

    return graph


def solve(file):
    lines = [[int(x) for x in line.strip()] for line in open(file)]
    start = (0, 0)
    graph = build_graph(lines)
    end = (max(x for x, y in graph.keys()), max(y for x, y in graph.keys()))
    risk = take_a_walk(graph, start, end)
    print("p1", risk)

    big_graph = build_graph(expand_map(lines))
    end = (max(x for x, y in big_graph.keys()), max(y for x, y in big_graph.keys()))
    risk = take_a_walk(big_graph, start, end)
    print("p2", risk)


if __name__ == '__main__':
    # solve("ex.txt")
    solve("in.txt")
