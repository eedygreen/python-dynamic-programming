from itertools import permutations

num_list = [2, 6, 7, 9]

for i, k in permutations(num_list, 2):
    print(f"{i=}, {k=}")