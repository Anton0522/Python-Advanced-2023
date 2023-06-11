numbers = tuple([float(x) for x in input().split()])

occ = {}

for el in numbers:
    if el not in occ:
        occ[el] = 0
    occ[el] += 1

for num, count in occ.items():
    print(f"{num} - {count} times")
