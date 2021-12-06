from collections import Counter

ex = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]

from collections import Counter

def part1(i):
    common, least = [], []
    zipped = list(zip(*[l for l in [[c for c in p] for p in i]]))
    for n in zipped:
        g = Counter(n)
        common.append(g.most_common()[0][0])
        least.append(g.most_common()[-1][0])

    print("1:", int("".join(common), 2) * int("".join(least), 2))


def zipped(l):
    return list(zip(*[l for l in [[c for c in p] for p in l]]))


def cleanup(k, v, l):
    new_list = []
    for i in l:
        if i[k] == v:
            new_list.append(i)
    return new_list


def part2(i):
    ll = i
    mm = i
    ind = 0
    while len(ll) > 1:
        z = zipped(ll)
        c = Counter(z[ind])
        m, l = c.most_common()[0][1], c.most_common()[1][1]
        a = "1" if m == l else c.most_common()[0][0]
        ll, ind = cleanup(ind, a, ll), ind+1

    ind = 0
    while len(mm) > 1:
        z = zipped(mm)
        c = Counter(z[ind])
        m, l = c.most_common()[0][1], c.most_common()[1][1]
        a = "0" if m == l else c.most_common()[1][0]
        mm, ind = cleanup(ind, a, mm), ind + 1

    print("2:", int(mm[0], 2) * int(ll[0], 2))


def solve():
    i = [str(line) for line in open("input.txt", "r")]
    part1(i)
    part2(i)


if __name__ == '__main__':
    solve()
