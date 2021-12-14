from collections import Counter


def do_count(ins):
    c = Counter(ins).values()
    return max(c) - min(c)


def find_rule(t, pairs):
    for p in pairs:
        if p[0] == t: return p[1]
    return None

def part1(template, pairs, steps=10):
    for _ in range(steps):
        inserted = []
        for i in range(len(template) - 1):
            t, s = template[i], template[i + 1]
            r = find_rule(f"{t}{s}", pairs)
            if r:
                inserted.append(f'{t}{r}')

        inserted.append(template[-1])
        template = "".join(inserted)

    c = Counter(template).values()
    return max(c) - min(c)


def part2(template, rules, steps):
    pc = Counter()
    for i in range(len(template) - 1):
        pc[template[i:i + 2]] += 1
    for _ in range(steps):
        n_pc = Counter()
        for pair, v in pc.items():
            l, r = pair[0], pair[1]
            for p, loc in rules:
                if pair == p:
                    n_pc[l + loc] += v
                    n_pc[loc + r] += v

        pc = n_pc
    counts = Counter()
    for k, v in pc.items():
        counts[k[0]] += v
    counts[template[-1]] += 1
    return max(counts.values()) - min(counts.values())


def read_input(file):
    lc = 0
    pairs = []
    template = ""
    with open(file) as f:
        for line in f:
            line = line.strip()
            if lc == 0:
                template = line
            elif lc > 1:
                sp = line.strip().split(" -> ")
                pairs.append((sp[0], sp[1]))
            lc += 1
    return template, pairs


def solve(file):
    t, p = read_input(file)
    print("p1", part1(t, p, steps=10))
    t, p = read_input(file)
    print("p2", part2(t, p, steps=40))


if __name__ == '__main__':
    # solve("ex.txt")
    solve("in.txt")
