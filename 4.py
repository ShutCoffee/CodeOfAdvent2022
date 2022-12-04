from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=4, year=2022)
data = data.splitlines()

# Part one
sum = 0
for line in data:
    elves = line.split(",")
    sections = elves[0].split("-") + elves[1].split("-")
    if int(sections[0]) <= int(sections[2]) and int(sections[1]) >= int(sections[3]):
        sum += 1
    elif int(sections[0]) >= int(sections[2]) and int(sections[1]) <= int(sections[3]):
        sum += 1

print(sum)

# Part two

def isOverlapping(start1, start2, end1, end2):
    assignment1 = [j for j in range(start1, end1+1)]
    assignment2 = [i for i in range(start2, end2+1)]
    return 1 if any(i in assignment1 for i in assignment2) else 0

sum = 0
for line in data:
    elves = line.split(",")
    sections = elves[0].split("-") + elves[1].split("-")
    sum += isOverlapping(int(sections[0]), int(sections[2]), int(sections[1]), int(sections[3]))

print(sum)