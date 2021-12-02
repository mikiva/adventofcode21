ex = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
]


def part1(i):
    hor, ver = 0, 0
    for a in i:
        if a[0] == "forward":
            hor += int(a[1])
        elif a[0] == "up":
            ver -= int(a[1])
        elif a[0] == "down":
            ver += int(a[1])

    print(hor * ver)


def part2(i):
    hor, ver, aim = 0, 0, 0
    for a in i:
        v = int(a[1])
        if a[0] == "forward":
            hor += v
            ver += aim * v
        elif a[0] == "up":
            aim -= v
        elif a[0] == "down":
            aim += v

    print(hor * ver)


def solve():
    i = [line for line in open("input.txt", "r")]
    i = [tuple(map(str, d.split(" "))) for d in i]
    part1(i)
    part2(i)


if __name__ == '__main__':
    solve()
