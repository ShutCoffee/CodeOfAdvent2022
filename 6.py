from aocd import get_data
from dotenv import load_dotenv
import numpy as np

load_dotenv()

data = get_data(day=6, year=2022)

# Part one
for i in range(4, len(data)):
    string = data[i-4:i]
    if len(set(string)) == len(string):
        print(i)
        break

# Part two
for i in range(14, len(data)):
    string = data[i-14:i]
    if len(set(string)) == len(string):
        print(i)
        break

