def generation(fish, p1, p2):
    d1, d2 = 0, 0
    nl = [0] * 10
    for f in fish:
        nl[f] += 1
    for day in range(p2):
        if day == p1:
            d1 = sum(nl)

        spawn = nl[0]
        for k in range(9):
            nl[k] = nl[k + 1]

        nl[6] += spawn
        nl[8] += spawn
    d2 = sum(nl)
    return d1, d2


def solve():
    with open("input.txt", "r") as inp:
        fish = [int(f) for f in inp.readline().split(",")]

    print("p1: {}, p2: {}".format(*generation(fish, 80, 256)))


if __name__ == '__main__':
    solve()
