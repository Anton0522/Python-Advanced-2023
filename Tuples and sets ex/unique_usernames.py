n = int(input())
my_set = set()

for _ in range(n):
    my_set.add(input())

print(*my_set, sep="\n")

# print({input() for _ in range(int(input()))}, sep="\n")

