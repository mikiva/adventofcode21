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
    for d, v in i:
        if d == "forward":
            hor += v
        elif d == "up":
            ver -= v
        elif d == "down":
            ver += v

    print(hor * ver)


def part2(i):
    hor, ver, aim = 0, 0, 0
    for d, v in i:
        if d == "forward":
            hor += v
            ver += aim * v
        elif d == "up":
            aim -= v
        elif d == "down":
            aim += v

    print(hor * ver)


def solve():
    i = [line for line in open("input.txt", "r")]
    i = [(d.split(" ")[0], int(d.split(" ")[1])) for d in i]
    part1(i)
    part2(i)


if __name__ == '__main__':
    solve()
