def do_fold(grid, dir, coor):
    folded = []
    if dir == "x":
        for g in grid:
            ind = coor
            t1 = g[:ind]
            t1.reverse()
            t2 = g[ind + 1:]
            for k, t in enumerate(t2):
                t1[k] = t if t2[k] == "#" else t1[k]
            t1.reverse()
            folded.append(t1)
    else:
        row = coor
        top = grid[:row]
        top.reverse()
        temp = []
        temp_bottom = grid[row + 1:]
        for i, b in enumerate(temp_bottom):
            t = top[i]
            for ii, bb in enumerate(b):
                t[ii] = "#" if bb == "#" else t[ii]
            temp.append(t)
        temp.reverse()
        folded = temp
    return folded


def fold(grid, dir, coor):
    if dir == "x":
        x = coor
        for g in grid:
            g[x] = "|"
    else:
        y = coor
        grid[y] = ["-" for _ in grid[y]]

    return do_fold(grid, dir, coor)


def part1(coors, instructions):
    xmin, xmax = 0, max(d[0] for d in coors)
    ymin, ymax = 0, max(d[1] for d in coors)
    grid = [["." for x in range(xmax + 1)] for y in range(ymax + 1)]

    for x, y in coors:
        grid[y][x] = "#"
    c = 0
    folds = 0
    for i in instructions:
        grid = fold(grid, i[0], i[1])
        folds += 1
        if folds == 1:
            for g in grid:
                c += sum([1 for l in g if l == "#"])

    print("p1", c)
    print("p2:")
    for g in grid:
        [print(l, end=" ") for l in g]
        print()


def solve(file):
    coors = []
    instructions = []
    with open(file) as f:
        for l in f:
            if l == "\n": continue
            if l.startswith("fold"):
                r = l.split("=")
                coor = int(r[1].strip())
                xy = r[0][-1]
                instructions.append((xy, coor))

            else:
                coors.append(tuple(int(j) for j in l.split(",")))
    part1(coors, instructions)


if __name__ == '__main__':
    # solve("ex.txt")
    solve("in.txt")
