from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=3, year=2022)
data = data.splitlines()

# Part one
sum = 0
for line in data:
    half = len(line)//2
    first = line[slice(0, half)]
    second = line[slice(half, len(line))]
    joint_letters = list(set(first)&set(second))
    for letter in joint_letters:
        if letter.isupper():
            sum += ord(letter) - 38
        else:
            sum += ord(letter) - 96

print(sum)


# Part two
sum = 0
for i in range(0, len(data), 3):
    joint_letters = list(set(data[i])&set(data[i+1])&set(data[i+2]))
    for letter in joint_letters:
        if letter.isupper():
            sum += ord(letter) - 38
        else:
            sum += ord(letter) - 96
print(sum)