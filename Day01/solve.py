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
    return sum([1 for k in range(len(m)) if ((m[k] - m[k - 1]) > 0)])


def part2(m):
    return sum([1 for k in range(len(m)) if (sum(m[k:k + 3]) < sum(m[k + 1:k + 4]))])


def solve():
    i = [int(line) for line in open("input.txt", "r")]
    print(part1(i))
    print(part2(i))


if __name__ == '__main__':
    solve()
