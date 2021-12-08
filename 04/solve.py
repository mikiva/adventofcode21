class Number:
    num: int
    drawn: bool = False

    def __init__(self, num):
        self.num = num

    def draw(self):
        self.drawn = True

    @property
    def is_drawn(self):
        return self.drawn


class Board:
    rows: [] = []
    last: int = None
    won: bool = False
    drawn: [] = []

    def __init__(self, rows):
        self.rows = rows

    @property
    def has_won(self):
        if self.last is not None:
            return True

        bb = self.rows
        for i in range(5):
            col = 0
            for b in bb:
                if b[i].is_drawn:
                    col += 1
            if col == 5:
                self.won = True
                return True
        for b in bb:
            if sum([1 for bd in b if bd.is_drawn]) == 5:
                self.won = True
                return True
        return False

    def draw(self, n):
        bb = self.rows
        for br in bb:
            if self.has_won:
                return
            for bn in br:
                if bn.num == n:
                    bn.draw()
                    if self.has_won:
                        self.last = n

    def not_drawn_sum(self):
        rows = self.rows
        unmarked = 0
        for row in rows:
            unmarked += sum([n.num for n in row if not n.is_drawn])
        return unmarked


def generate_boards(inp):
    boards = []
    board = []
    for line in inp:
        if line.startswith('\n'):
            boards.append(Board(board))
            board = []
        else:
            board.append([Number(num=int(l)) for l in line.strip().split()])
    boards.append(Board(board))

    return boards


def part1(nn, bb):
    for n in nn:
        for b in bb:
            b.draw(n)
            if b.has_won:
                return b


def part2(nn, bb):
    won_boards = []
    for n in nn:
        for b in bb:
            if b.last is None:
                b.draw(n)
                if b.last is not None:
                    won_boards.append(b)

    return won_boards[-1]


def solve():
    i = [line for line in open("input.txt", "r")]
    drawn = [int(d) for d in i[0].split(",")]
    boards = generate_boards(i[2:])

    p1 = part1(drawn, boards)
    print("p1: ", p1.not_drawn_sum() * p1.last)

    p2 = part2(drawn, boards)
    print("p2: ", p2.not_drawn_sum() * p2.last)


if __name__ == '__main__':
    solve()
