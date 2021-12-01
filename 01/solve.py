example = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263
]


def part1(m):
    i = 0
    for k in range(len(m)):
        i = i + 1 if ((m[k] - m[k - 1]) > 0) else i
    return i


def part2(m):
    i = 0
    for k in range(len(m) - 3):
        a = m[k] + m[k + 1] + m[k + 2]
        b = m[k + 1] + m[k + 2] + m[k + 3]
        i = i + 1 if a < b else i

    return i


def solve():
    i = [int(line) for line in open("input.txt", "r")]
    print(part1(i))
    print(part2(i))


if __name__ == '__main__':
    solve()
