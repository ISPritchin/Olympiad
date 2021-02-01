def input_matrix(n, f=int):
    matrix = []
    for i in range(n):
        matrix.append(input())
    return matrix


def is_sim3_3(a):
    if a[0] == a[2][::-1] and a[1][0] == a[1][2]:
        print("YES")
    else:
        print("NO")


is_sim3_3(input_matrix(3))
