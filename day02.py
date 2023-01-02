rounds = open("day02.txt").read().split("\n")

rock = "r"
paper = "p"
scissors = "s"
win = "W"
draw = "D"
lose = "L"

scoring = {
    rock: 1,
    paper: 2,
    scissors: 3,
    win: 6,
    draw: 3,
    lose: 0
}

code1 = {"A": rock, "B": paper, "C": scissors, "X": rock, "Y": paper, "Z": scissors }
code2 = {"A": rock, "B": paper, "C": scissors, "X": lose, "Y": draw, "Z": win }

rules = {
    rock: {
        rock: draw, paper: win, scissors: lose,
        draw: rock, win: paper, lose: scissors
    },
    paper: {
        rock: lose, paper: draw, scissors: win,
        lose: rock, draw: paper, win: scissors
    },
    scissors: {
        rock: win, paper: lose, scissors: draw,
        win: rock, lose: paper, draw: scissors
    },
}

score1 = 0
score2 = 0

for round in rounds:
    [opp, me] = round.split(" ")
    score1 += scoring[rules[code1[opp]][code1[me]]] + scoring[code1[me]]
    score2 += scoring[rules[code2[opp]][code2[me]]] + scoring[code2[me]]

print("Rounds Played:", len(rounds))
print("Code 1:", score1)
print("Code 2:", score2)
