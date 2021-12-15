import sys


def part1(ll):
    finished = False
    start = (0, 0)
    current = start
    steps = []


right = (0, 1)
left = (0, -1)
down = (1, 0)
up = (-1, 0)
end = ()
start = (0, 0)
lowest = sys.maxsize


def find_path(ll, ex, ey):
    c = [[0 for x in y] for y in ll]

    c[0][0] = ll[0][0]


def is_inside(ss, c):
    return 0 <= c[0] < len(ss) and 0 <= c[1] < len(ss[0])


def check_step(ss, c, seen):
    # if is_out(ss, c):
    #   return sys.maxsize
    if c == end:
        r = ss[c[0]][c[1]]
        print(c)
        print("RRR", r)
        return r

    seen.add(c)
    risk = 0
    # for i, s in enumerate(ss):
    #    for j, t in enumerate(s):
    #        risk += min(check_step(ss, (i + 1, j), seen), check_step(ss, (i, j + 1), seen))
    # return risk
    checks = []
    tu, tl, tr, td = c, c, c, c
    while len(checks) < 1:
        tu = tuple(map(lambda i, j: i + j, c, up))
        tl = tuple(map(lambda i, j: i + j, c, left))
        tr = tuple(map(lambda i, j: i + j, c, right))
        td = tuple(map(lambda i, j: i + j, c, down))
        if is_inside(ss, tu) and tu not in seen:
            # risk += check_step(ss, tu, seen)
            checks.append(tu)
        if is_inside(ss, td) and td not in seen:
            # risk += check_step(ss, td, seen)
            checks.append(td)
        if is_inside(ss, tr) and tr not in seen:
            # risk += check_step(ss, tr, seen)
            checks.append(tr)
        if is_inside(ss, tl) and tl not in seen:
            # risk += check_step(ss, tl, seen)
            checks.append(tl)
        # print(checks, tu, tr, td, tl, c)
        if not checks:
            continue
        return ss[c[0]][c[1]] + min([check_step(ss, st, seen) for st in checks])


from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)

        self.distances = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def minCost(cost, m, n, width, height):
    #print(m,n, width, height)
    if n > width or m > height:
        return sys.maxsize
    elif (m == width and n == height):
        return cost[m][n]
    else:
        return cost[m][n] + min(minCost(cost, m + 1, n, width, height),
                                minCost(cost, m, n + 1, width, height))


# A utility function that returns minimum of 3 integers */
# def min(x, y, z):
#    if (x < y):
#        return x if (x < z) else z
#    else:
#        return y if (y < z) else z


def solve(file):
    lines = []
    with open(file, "r") as inp:
        for line in inp:
            lines.append([int(l) for l in [k for k in line.strip()]])

    width = len(lines[0]) - 1
    height = len(lines) - 1
    global end
    start = (0, 0)
    x, y = width, height
    end = (x, y)
    empty_grid = [[0] * len(lines[0]) for _ in range(len(lines))]

    print(x, y)
    cost = minCost(lines, 0, 0, width, height) - lines[0][0]
    print(cost)

#    risk = check_step(lines, start, set())
#    print(risk)
# find_path(lines, x, y)


#    part1(lines)

if __name__ == '__main__':
    #solve("ex.txt")
    solve("in.txt")
