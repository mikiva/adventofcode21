import sys

tx = []
ty = []
maxx = sys.maxsize
miny = -maxx


def launch(x, y):
    pos = (0, 0)
    hy = 0
    while True:
        np = (pos[0] + x, pos[1] + y)
        if np[1] > hy:
            hy = np[1]

        if np[0] in tx and np[1] in ty:
            return hy, True
        elif np[0] > maxx or np[1] < miny:
            return -sys.maxsize, False

        if abs(x) > 0:
            if x > 0:
                x -= 1
            else:
                x += 1
        y -= 1
        pos = np


def solve(file):
    global tx, ty, maxx, miny
    line = open(file).readline()
    targets = line[13:].strip().split(", ")
    xxs = [int(x) for x in targets[0].split("=")[1].split("..")]
    yys = [int(y) for y in targets[1].split("=")[1].split("..")]
    tx = [xxs[0] + i for i in range(abs(xxs[0] - xxs[1]) + 1)]
    ty = [yys[0] + i for i in range(abs(yys[0] - yys[1]) + 1)]

    maxx = max(tx)
    miny = min(ty)
    hy = 0
    valid = set()
    for x in range(-200, maxx+1):
        for y in range(miny, 200):
            h, goal = launch(x, y)
            hy = h if h > hy else hy
            if goal:
                valid.add((x, y))

    print("p1", hy)
    print("p2", len(valid))


if __name__ == '__main__':
    # solve("ex.txt")
    solve("in.txt")
