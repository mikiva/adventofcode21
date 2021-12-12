from collections import defaultdict

uni = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}


class Display:
    pass


def part1(ll):
    unique_uses = 0
    for l in ll:
        unique_uses += sum([1 for s in l if len(set(s)) in uni])

    return unique_uses


def get_uniq(ll):
    d = defaultdict(set)
    for s in ll:
        le = len(set(s))
        if le in uni:
            d[uni[le]] = set(s)

    return d


def part2(ll):
    last = 0
    for l, o in ll:
        words = []
        for sl in l:
            words.append(sl)
        d = get_uniq(words)
        for word in words:
            if len(word) == 5 and d[1].intersection(set(word)) == d[1]:
                d[3] = set(word)

        dd = d[3].intersection(d[4] - d[1])  # middle hor
        bb = (d[4] - d[1]) - set(dd)  # up left ver
        for word in words:
            if len(word) == 5 and set(word) != d[3]:
                if bb.intersection(set(word)) == set():
                    d[2] = set(word)
                else:
                    d[5] = set(word)

            elif len(word) == 6:
                if set(word).intersection(dd) == set():
                    d[0] = set(word)

                if d[4].intersection(set(word)) == d[4]:
                    d[9] = set(word)
                elif len(d[7].intersection(set(word))) == 2:
                    d[6] = set(word)
        ans = o
        disp = ""
        for a in ans:
            for dk, dv in d.items():
                if sorted(dv) == sorted(set(a)):
                    disp += str(dk)

        assert len(disp) == 4
        last += int(disp)

    return last


def solve(file):
    lines = []
    p1 = []
    ll = [l for l in open(file).read().split("\n")]
    for l in ll:
        i, o = l.split(" | ")[0], l.split(" | ")[1]

        i, o = i.split(" "), o.split(" ")
        lines.append((i, o))
        p1.append(o)
    print("p1", pt1 := part1(p1))
    print("p2", pt2 := part2(lines))
    return pt1, pt2


if __name__ == '__main__':
    assert solve("exinput.txt") == (26, 61229)
    solve("input.txt")