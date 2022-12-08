from aocd import get_data
from dotenv import load_dotenv
import numpy as np

load_dotenv()

data = get_data(day=7, year=2022)
data = data.splitlines()

directory_path = []
filesize_directory = {}

i = 0
while(i < len(data)):
    line = data[i]
    if line[0] == '$':
        a = line.split(" ")
        if a[1] == "cd":
            if a[2] != "..":
                curr_dir = '/'.join(directory_path) + '/' + a[2]
                directory_path.append(curr_dir)
                if a[2] not in filesize_directory.keys():
                    filesize_directory[curr_dir] = 0
            else:
                del directory_path[-1]
    elif line[0].isnumeric():
        for dir in directory_path:
            filesize_directory[dir] += int(line.split(" ")[0])
    i += 1


# Part one
print((sum([v for _, v in filesize_directory.items() if v <= 100000])))

# Part two
needed_space = filesize_directory["//"] - 40000000
possible_candidates = [v for v in filesize_directory.values() if v > needed_space]
dict_to_delete = min(possible_candidates)
print(dict_to_delete)