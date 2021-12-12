from collections import defaultdict

START = "start"
END = "end"


def deeper(graph, curr, seen, revisit):
    if curr == END: return 1
    c = 0
    new_seen = seen | {curr} if curr.islower() else seen

    for n in graph[curr]:
        if n == START: continue
        if n in seen:
            if not revisit: continue
            c += deeper(graph, n, new_seen, False)
        else:
            c += deeper(graph, n, new_seen, revisit)
    return c


def build_graph(ll):
    d = defaultdict(list)
    for l in ll:
        a, b = l[0], l[1]
        d[a].append(b)
        d[b].append(a)
    return d


def go_deeper(ll):
    d = build_graph(ll)
    paths1 = deeper(d, START, set(), False)
    paths2 = deeper(d, START, set(), True)
    print("p1", paths1)
    print("p2", paths2)


def solve(file):
    i = [tuple(l.split("-")) for l in open(file).read().split("\n")]
    go_deeper(i)


if __name__ == '__main__':
    # solve("exsm.txt")
    # solve("exlg.txt")
    # solve("ex.txt")
    solve("in.txt")
