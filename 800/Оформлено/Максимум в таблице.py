n = int(input())
x = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    x[i][0] = 1
    x[0][i] = 1
for i in range(1, n):
    for j in range(1, n):
        x[i][j] = x[i-1][j] + x[i][j-1]
print(x[-1][-1])
