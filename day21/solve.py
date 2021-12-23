class Player:
    position: int
    score: int

    def __init__(self, pos, scr):
        self.position = pos
        self.score = scr

    @property
    def has_won(self):
        return self.score >= 1000

    def add_score(self):
        self.score += self.position
        return self.has_won

    def move(self, steps: int):
        for _ in range(1, steps + 1):
            self.position += 1
            if self.position > 10:
                self.position = 1

        return self.add_score()

    def __str__(self):
        return str(self.score)


class Die:
    current: int = 0
    rolls = 0

    @property
    def roll(self):
        steps = 0
        for _ in range(3):
            self.current += 1
            self.rolls += 1
            if self.current > 100:
                self.current = 1
            steps += self.current
        return steps


def solve(file):
    lines = open(file).read().split("\n")
    _, p1 = [int(i) for i in lines[0].split() if i.isdigit()]
    _, p2 = [int(i) for i in lines[1].split() if i.isdigit()]

    player1 = Player(p1, 0)
    player2 = Player(p2, 0)
    die = Die()
    winner = False
    while not winner:
        if player1.move(die.roll):
            winner = True
        elif player2.move(die.roll):
            winner = True

    part1 = min(player1.score, player2.score) * die.rolls
    print("p1", part1)


if __name__ == '__main__':
    #solve("ex.txt")
    solve("in.txt")
