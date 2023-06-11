rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

for col_idx in range(cols):
    sum_elements = 0
    for row_idx in range(rows):
        sum_elements += matrix[row_idx][col_idx]
    print(sum_elements)
