from functools import reduce
import operator

mm = []


def get_lowpoints():
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    lowpoints = []
    lp_coors = []
    for mk, mv in enumerate(mm):
        for lk, lv in enumerate(mv):
            is_low = True
            for d in dirs:
                if 0 <= (mk + d[0]) < len(mm) and 0 <= (lk + d[1]) < len(mv):
                    if lv >= mm[mk + d[0]][lk + d[1]]:
                        is_low = False
                        break
            if is_low:
                lowpoints.append(lv)
                lp_coors.append((mk, lk))
    return lowpoints, lp_coors


def part1():
    lowpoints, _ = get_lowpoints()
    lp = sum([l + 1 for l in lowpoints])
    return lp


def check_basin(coors, b):
    x, y = coors[0], coors[1]
    if mm[x][y] in [-1, 9]:
        return False

    mm[x][y] = -1
    b.add((x, y))
    if (x < (len(mm) - 1) and check_basin((x + 1, y), b)) or (
        y > 0 and check_basin((x, y - 1), b)) or (x > 0 and check_basin((x - 1, y), b)) or (
        y < len(mm[x]) - 1 and check_basin((x, y + 1), b)):
        return True
    else:
        return False


def part2():
    lowpoints, coors = get_lowpoints()
    basins = []
    for c in coors:
        b = set()
        check_basin(c, b)
        basins.append(len(b))

    return reduce(operator.mul, sorted(basins, reverse=True)[:3], 1)


def print_seafloor():
    nm = []
    for m in mm:
        ss = []
        for s in m:
            t = "-" if s == -1 else "X"
            ss.append(t)
        nm.append(ss)

    nm = ["".join(m) for m in nm]
    nm = "\n".join(nm)
    print("Sea floor:\n", nm)
    with open("out.txt", "w") as out:
        out.write(nm)



def solve(file):
    global mm
    i = [l for l in open(file).read().split("\n")]
    mm = [[int(n) for n in l] for l in i]
    print("p1: ", part1())
    print("p2: ", part2())
    print_seafloor()


if __name__ == '__main__':
    # solve("ex.txt")
    solve("in.txt")
