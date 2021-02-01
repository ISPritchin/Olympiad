def input_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix


def get_sum_in_row(a, i):
    return sum(a[i])


def get_sum_in_col(a, j):
    return sum((a[i][j] for i in range(len(a))))


n = int(input())
a = input_matrix(n)
row_sums = [get_sum_in_row(a, i) for i in range(n)]
col_sums = [get_sum_in_col(a, j) for j in range(n)]

n_ceil = 0
for row_sum in row_sums:
    for col_sum in col_sums:
        if col_sum > row_sum:
            n_ceil += 1
print(n_ceil)