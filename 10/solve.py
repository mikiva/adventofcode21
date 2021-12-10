from collections import defaultdict

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
p2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

co = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

cop = ["(", "[", "{", "<"]


def get_invalid(m):
    o = []
    for c in m:
        if c in cop:
            o.append(c)
        else:
            cl = o.pop()
            if co[cl] != c:
                return c


def get_rest(m):
    o = []
    for c in m:
        if c in cop:
            o.append(c)
        else:
            o.pop()
    rest = [co[c] for c in o[::-1]]
    return rest


def sort_lines(mm):
    invalids = []
    incomplete = []
    for m in mm:
        if invalid := get_invalid(m):
            invalids.append(invalid)
        else:
            incomplete.append(m)

    # PART1
    score = 0
    for inv in invalids:
        p = points[inv]
        score += p
    print("p1", score)
    # PART2
    s2 = []
    for inc in incomplete:
        s = 0
        rest = get_rest(inc)
        for r in get_rest(inc):
            s *= 5
            s += p2[r]
        s2.append(s)
    score2 = sorted(s2)[(len(s2) - 1) // 2]
    print("p2", score2)


def solve(file):
    i = [l for l in open(file).read().split("\n")]
    mm = [[n for n in l] for l in i]

    sort_lines(mm)


if __name__ == '__main__':
    # solve("ex.txt")
    solve("in.txt")
