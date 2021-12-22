checks = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


def pg(grid):
    for g in grid:
        print("".join([x for x in g]))


def enhance(orig, alg, times):
    default = "0"
    for _ in range(times):
        rows = len(orig)
        cols = len(orig[0])
        enhanced_image = [["." for _ in range(rows + 2)] for _ in range(cols + 2)]

        for x in range(-1, rows + 1):
            for y in range(-1, cols + 1):

                bin = ""
                for dx, dy in checks:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        bin += "1" if orig[nx][ny] == "#" else "0"
                    else:
                        bin += default

                enhanced_image[x + 1][y + 1] = alg[int(bin, 2)]
        default = "1" if alg[int((default * 9), 2)] == "#" else "0"
        print(default)
        orig = enhanced_image
    return orig


def create_grid(input_image):
    grid = [["." for _ in range(len(input_image) + 2)] for _ in range(len(input_image[0]) + 2)]

    for x, r in enumerate(input_image):
        for y, c in enumerate(r):
            grid[x + 1][y + 1] = c

    for g in grid:
        print("".join([str(x) for x in g]))
    return grid


def solve(file):
    alg, inp = open(file).read().split("\n\n")
    alg = "".join(alg.strip().split("\n"))
    inp = [[y for y in x] for x in inp.strip().split("\n")]
    input_image = []
    for i, row in enumerate(inp):
        r = []
        for j, col in enumerate(row):
            r.append(col)

        input_image.append(r)

    new_grid_1 = enhance(input_image, alg, 2)
    new_grid_2 = enhance(input_image, alg, 50)

    c1 = 0
    for g in new_grid_1:
        c1 += sum([1 for c in g if c == "#"])
    c2 = 0
    for g in new_grid_2:
        c2 += sum([1 for c in g if c == "#"])
    #pg(new_grid_2)
    print("p1", c1)
    print("p2", c2)


if __name__ == '__main__':
    #solve("ex.txt")
    solve("in.txt")
