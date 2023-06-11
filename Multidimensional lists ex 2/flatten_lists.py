line = input().split("|")

sub_lists =[]

for string in line[::-1]:
    sub_lists.extend(string.split())

print(*sub_lists)

