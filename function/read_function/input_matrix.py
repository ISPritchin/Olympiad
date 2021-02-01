def input_matrix(n, f=int):
    matrix = []
    for i in range(n):
        matrix.append(list(map(f, input().split())))
    return matrix
