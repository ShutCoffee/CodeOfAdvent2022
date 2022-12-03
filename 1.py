from aocd import get_data
from dotenv import load_dotenv

load_dotenv()

data = get_data(day=1, year=2022)
data = data.splitlines()

# Part one
max_sum = 0
sum = 0
for line in data:
    if line == '':
        if max_sum < sum:
            max_sum = sum
        sum = 0
    else:
        sum += int(line)

print(max_sum)

# Part two
sum = 0
second_sum = 0
third_sum = 0
for line in data:
    if line == "":
        if third_sum < sum and sum < max_sum:
            if second_sum < sum:
                second_sum = sum
            else:
                third_sum = sum
        sum = 0
    else:
        sum += int(line)

three_most = max_sum + second_sum + third_sum
print(three_most)