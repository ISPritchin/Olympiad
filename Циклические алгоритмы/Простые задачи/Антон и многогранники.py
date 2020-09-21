# https://codeforces.com/problemset/problem/785/A

n = int(input())
res = 0
for i in range(n):
    f = input()
    if f == "Tetrahedron":
        res += 4
    elif f == "Cube":
        res += 6
    elif f == "Octahedron":
        res += 8
    elif f == "Dodecahedron":
        res += 12
    else:
        res += 20
print(res)
