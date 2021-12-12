import sys


def do_align2(coors, l, current):
    cost = 0
    for c in coors:
        distance = abs(c - l)
        for d in range(distance):
            cost += (1 + d)
            if cost >= current:
                return sys.maxsize
    return cost


def part1(coors):
    minc, maxc, fuel = min(coors), max(coors), sys.maxsize
    for l in range(minc, maxc):
        cost = sum([abs(c - l) for c in coors])
        fuel = cost if (cost < fuel) else fuel

    print("P1: ", fuel)
    return fuel


def part2(coors):
    minc, maxc, fuel = min(coors), max(coors), sys.maxsize
    for l in range(minc, maxc):
        cost = do_align2(coors, l, fuel)
        fuel = cost if (cost < fuel) else fuel

    print("P2: ", fuel)
    return fuel


def solve():
    with open("input.txt", "r") as inp:
        i = [int(l) for l in inp.readline().split(",")]
    assert part1(i) == 359648
    assert part2(i) == 100727924


if __name__ == '__main__':
    solve()
