from aocd import get_data
from dotenv import load_dotenv
import numpy as np

load_dotenv()

data = get_data(day=8, year=2022)

# test_data = """30373
# 25512
# 65332
# 33549
# 35390
# """
# data = test_data

data = data.splitlines()
data = np.array([list(i) for i in data], int)

part1 = np.zeros_like(data, int)
part2 = np.ones_like(data, int)

for _ in range(4):
    for x,y in np.ndindex(data.shape):   
            lower = [t < data[x,y] for t in data[x,y+1:]]

            part1[x,y] |= all(lower)
            part2[x,y] *= next((i+1 for i,t in enumerate(lower) if ~t), len(lower))

    data, part1, part2 = map(np.rot90, [data, part1, part2])

print(part1.sum(), part2.max())



