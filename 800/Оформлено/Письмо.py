def input_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append(input())
    return matrix


def clear(a):
    i = 0
    while "*" not in a[i]:
        i += 1
    j = len(a) - 1
    while "*" not in a[j]:
        j -= 1
    return a[i:j + 1]


n, m = map(int, input().split())
a = clear(input_matrix(n))

left = m - 1
right = 0
for x in a:
    if "*" in x:
        left = min(left, x.find("*"))
        right = max(right, x.rfind("*"))

for x in a:
    print(x[left:right + 1], sep="")
