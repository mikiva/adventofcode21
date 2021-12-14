from collections import Counter


def do_count(ins):
    c = Counter(ins).values()
    return max(c) - min(c)


def find_rule(t, pairs):
    for p in pairs:
        if p[0] == t: return p[1]
    return None



"""
part1 Arkvierad pga ung och naiv
"""
#def part1(template, pairs, steps=10):
#    for _ in range(steps):
#        inserted = []
#        for i in range(len(template) - 1):
#            t, s = template[i], template[i + 1]
#            r = find_rule(f"{t}{s}", pairs)
#            if r:
#                inserted.append(f'{t}{r}')
#
#        inserted.append(template[-1])
#        template = "".join(inserted)
#
#    c = Counter(template).values()
#    return max(c) - min(c)



def insertion(template, rules, steps):
    pc = Counter()
    for i in range(len(template) - 1):
        pc[template[i:i + 2]] += 1
    for s in range(steps):
        if s == 10:
            print_count("p1", pc, template)
        n_pc = Counter()
        for pair, v in pc.items():
            l, r = pair[0], pair[1]
            for p, loc in rules:
                if pair == p:
                    n_pc[l + loc] += v
                    n_pc[loc + r] += v

        pc = n_pc

    print_count("p2", pc, template)

def print_count(part, c, template):
    counts = Counter()
    for k, v in c.items():
        counts[k[0]] += v
    counts[template[-1]] += 1
    solution = max(counts.values()) - min(counts.values())

    print(f"{part}: {solution}")


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
    insertion(t, p, steps=40)


if __name__ == '__main__':
    # solve("ex.txt")
    solve("in.txt")
