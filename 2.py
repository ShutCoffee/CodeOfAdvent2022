from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=2, year=2022)
data = data.splitlines()

# Part one
win_scenarios = ["A Y", "B Z", "C X"]
draw_scenarios = ["A X", "B Y", "C Z"]

sum = 0
for line in data:
    my_shape = line[-1]
    if my_shape == "X":
        sum += 1
    elif my_shape == "Y":
        sum += 2
    elif my_shape == "Z":
        sum += 3

    if line in win_scenarios:
        sum += 6
    elif line in draw_scenarios:
        sum += 3

print(sum)

# Part two
comb = {"A": {"X": "scissors", "Y": "rock", "Z": "paper"}, 
                "B": {"X": "rock", "Y": "paper", "Z": "scissors"},
                "C": {"X": "paper", "Y": "scissors", "Z": "rock"}}
points = {"scissors": 3, "paper": 2, "rock": 1, "X": 0, "Y": 3, "Z": 6}
sum = 0
for line in data:
    result = line[-1]
    opponent = line[0]
    to_play = comb[opponent][result]
    sum += points[to_play] + points[result]

print(sum)
