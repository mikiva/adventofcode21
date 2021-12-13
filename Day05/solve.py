class Coor:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x, self.y}"


class Line:
    fr: Coor
    to: Coor

    def __init__(self, f, t):
        self.fr = Coor(int(f[0]), int(f[1]))
        self.to = Coor(int(t[0]), int(t[1]))

    @property
    def is_right_angle(self):
        return self.fr.x == self.to.x or self.fr.y == self.to.y

    @property
    def is_diagonal(self):
        diag = abs(self.fr.x - self.to.x) == abs(self.fr.y - self.to.y)
        return diag

    @property
    def is_vertical(self):
        return self.fr.x == self.to.x

        pass

    def __str__(self):
        return f"line x, y: {(self.fr.x, self.fr.y)}, {(self.to.x, self.to.y)}"


def get_input() -> [Line]:
    i = [tuple(line.strip().split("->")) for line in open("input.txt", "r")]
    lines =[]
    for l in i:
        lines.append(Line(tuple(l[0].strip().split(',')), tuple(l[1].strip().split(','))))
    return lines


def plot_lines(grid, line):
    fr = line.fr
    to = line.to

    tf_x = (fr.x, to.x) if fr.x < to.x else (to.x, fr.x)
    tf_y = (fr.y, to.y) if fr.y < to.y else (to.y, fr.y)
    for x in range(tf_x[0], tf_x[1] + 1):
        for y in range(tf_y[0], tf_y[1] + 1):
            grid[y][x] += 1


def plot_diagonal(grid, line):
    f = line.fr
    t = line.to
    if f.x > t.x:
        f, t = t, f

    dir = -1 if f.y > t.y else 1
    y = f.y
    for x in range(f.x, t.x + 1):
        grid[y][x] += 1
        y = y + dir


def part1():
    lines = get_input()
    max_x, max_y = 0, 0
    for l in lines:
        max_x = max(max_x, l.fr.x, l.to.x)
        max_y = max(max_y, l.fr.y, l.to.y)
    lines = [l for l in lines if l.is_right_angle]

    grid = [[0 for col in range(max_x + 1)] for row in range(max_y + 1)]

    for line in lines:
        plot_lines(grid, line)

    over_two = 0
    for row in grid:
        for col in row:
            if col >= 2:
                over_two += 1
    print("p1: ", over_two)


def part2():
    lines = get_input()
    max_x, max_y = 0, 0
    for l in lines:
        max_x = max(max_x, l.fr.x, l.to.x)
        max_y = max(max_y, l.fr.y, l.to.y)
    grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]


    lines = [l for l in lines if l.is_right_angle]


    for line in lines:
        plot_lines(grid, line)

    lines = get_input()
    lines = [l for l in lines if l.is_diagonal]
    for line in lines:
        plot_diagonal(grid, line)

    over_two = 0
    for row in grid:
        for col in row:
            if col >= 2:
                over_two += 1
    print("p2: ", over_two)


def solve():
    part1()
    part2()


if __name__ == '__main__':
    solve()
