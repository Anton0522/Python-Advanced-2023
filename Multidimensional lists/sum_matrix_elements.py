rows, cols = [int(el) for el in input().split(", ")]
matrix = []

for _ in range(rows):
    inner_list = []
    numbers_as_strings = input().split(", ")

    for num_as_str in numbers_as_strings:
        inner_list.append(int(num_as_str))

    matrix.append(inner_list)

sum_numbers = 0

for row_index in range(rows):
    for col_index in range(cols):
        sum_numbers += matrix[row_index][col_index]

print(sum_numbers)
print(matrix)
