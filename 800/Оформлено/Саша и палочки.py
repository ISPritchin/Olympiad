n, k = map(int, input().split())
n_h = n // k
if n_h % 2 == 0:
    print("NO")
else:
    print("YES")
