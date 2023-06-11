rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    inner_list = [int(el)for el in input().split(", ")]
    matrix.append(inner_list)

max_sum = -99999999999999 # define very low number
sub_matrix = []
sum_elements = 0
for row_idx in range(rows):
    for col_idx in range(cols - 1):
        current_el = matrix[row_idx][col_idx]
        element_below = matrix[row_idx+1][col_idx]
        next_el = matrix[row_idx][col_idx+1]
        diagonal_el = matrix[row_idx+1][col_idx+1]
        sum_elements = current_el + element_below + next_el + diagonal_el
        if max_sum < sum_elements:
            max_sum = sum_elements
            sub_matrix = [[current_el, next_el, element_below, diagonal_el]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(sum_elements)