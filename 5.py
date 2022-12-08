from aocd import get_data
from dotenv import load_dotenv
import numpy as np

load_dotenv()

data = get_data(day=5, year=2022)
data = data.splitlines()

starting_position = []
instructions = []

# add data to the correct arrays
i = 0
while( "[" in data[i] ):
    starting_position.append(data[i].split(" "))
    i += 1

i += 2 #
while(i < len(data)):
    instructions.append(data[i])
    i += 1


# parse both arrays into better format
parsed_starting_position = []
for position in starting_position:
    i = 0
    stack = []
    while i < len(position):
        stack.append(position[i])
        if position[i] == "":
            i += 3
        i += 1
    parsed_starting_position.append(stack)

parsed_instructions = []
for instruction in instructions:
    inst = instruction.split(" ")
    parsed_instructions.append([int(inst[1]), int(inst[3]), int(inst[5])])


np_instructions = np.array(parsed_instructions)

# transpose so that each array represents a stack
np_starting_positions = np.array(parsed_starting_position).T
np_starting_positions = np_starting_positions.tolist()

# remove empty strings and empty stacks
starting_postitions = []
for position in np_starting_positions:
    pos = []
    for i, element in enumerate(position):
        if element != "":
            pos.append(element)
    if len(pos) != 0:
        starting_postitions.append(pos)

np_starting_positions = starting_postitions

# part one
# for instruction in np_instructions:
#     i = instruction[0]
#     while(i > 0):
#         element = np_starting_positions[instruction[1]-1].pop(0)
#         np_starting_positions[instruction[2]-1].insert(0, element)
#         i -= 1

# for position in np_starting_positions:
#     print(position[0], end="")
# print("\n")

# part two (part one needs to be commented out so that this part works)
for instruction in np_instructions:
    i = instruction[0]
    removed_items = np_starting_positions[instruction[1]-1][:i]
    del np_starting_positions[instruction[1]-1][:i]
    for item in reversed(removed_items):
       np_starting_positions[instruction[2]-1].insert(0, item)

for position in np_starting_positions:
    print(position[0], end="")