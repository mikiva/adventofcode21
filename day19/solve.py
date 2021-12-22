
def parseScanners(file):
    with open(file) as i:
        sin = i.read().split("\n\n")
        scanners = [[tuple(map(int, s.split(","))) for s in group.split("\n")[1:]] for group in sin]
        return scanners



def solve(file):
    scanners = parseScanners(file)



if __name__ == '__main__':
    solve("ex.txt")
    #solve("exsm.txt")
    #solve("in.txt")
