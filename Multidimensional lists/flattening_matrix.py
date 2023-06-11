row = int(input())
flatten = []
for row_idx in range(row):
    inner_list = [int(el) for el in input().split(", ")]
    flatten.extend(inner_list)

print(flatten)

#   matrix.append(inner_list)

#for row_idx in range(len(matrix)):
#   for col_idx in range(len(matrix[row_idx])):
#       flatten.append(matrix[row_idx][col_idx])