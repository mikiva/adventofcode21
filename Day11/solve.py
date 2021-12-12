dirs = [(-1, 0), (0, -1), (0, 1), (1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]


class Octopus:
    lvl: int
    flashed: bool = False

    def __init__(self, lvl):
        self.lvl = lvl

    def add(self):
        self.lvl += 1

    def flash(self):
        self.flashed = True

    def reset(self):
        self.lvl = 0
        self.flashed = False

    def __str__(self):
        return str(self.lvl)

def increase_one(mm):
    for m in mm:
        for o in m:
            o.add()

def add_around(x, y, mm):
    for d in dirs:
        if 0 <= (x + d[0]) < (len(mm[x])) and 0 <= (y + d[1]) < len(mm[x]):
            mm[x + d[0]][y + d[1]].add()


def check_flashes(mm):
    flashing = True
    while flashing:
        flashing = False
        for kx, vx in enumerate(mm):
            for ky, vy in enumerate(vx):
                if vy.lvl > 9 and not vy.flashed:
                    flashing = True
                    add_around(kx, ky, mm)
                    vy.flash()

    flashes = 0
    for m in mm:
        for o in m:
            if o.flashed:
                flashes += 1
                o.reset()
    return flashes


def start_flashing(mm):
    flashes = 0
    step = 0
    simultaneously = False
    while not simultaneously:
        increase_one(mm)
        new_flashes = check_flashes(mm)
        if step < 100:
            flashes += new_flashes
        if new_flashes >= 10 * 10:
            simultaneously = True
        step += 1

    print("Part 1: ", flashes)
    print("Part 2: ", step)
    return flashes


def solve(file):
    i = [l for l in open(file).read().split("\n")]
    mm = [[Octopus(lvl=int(n)) for n in l] for l in i]
    start_flashing(mm)


if __name__ == '__main__':
    # solve("exsm.txt")
    # solve("ex.txt")
    solve("in.txt")
