from copy import copy
from collections import defaultdict


def part2(fish):
    day = 0
    fd = defaultdict(int)
    for f in fish:
        fd[f] += 1
    print(fd)
    while day < 80:
        nfd = copy(fd)
        for k in fd.keys():
            if k == 0:
                if nfd[0] > 0:
                    nfd[0] -= 1
                    nfd[6] += 1
                    nfd[8] += 1
            elif k > 0:
                if nfd[k] > 0:
                    nfd[k] -= 1
                    nfd[k - 1] += 1
        fd = copy(nfd)
        day += 1
    print(fd)
    print("p2: ", sum(fd.values()))


def part1(fish):
    day = 0
    while day < 80:
        new_day = copy(fish)
        for k, f in enumerate(fish):
            if f == 0:
                new_day.append(8)
                new_day[k] = 6
            else:
                new_day[k] = f - 1
        fish = copy(new_day)
        day += 1
    print("p1: ", len(fish))


def solve():
    with open("exinput.txt", "r") as inp:
        fish = [int(f) for f in inp.readline().split(",")]

    part1(fish)
    part2(fish)


if __name__ == '__main__':
    solve()
