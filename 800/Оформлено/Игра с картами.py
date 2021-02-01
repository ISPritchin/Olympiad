n_sets = int(input())
for i in range(n_sets):
    n, k1, k2 = map(int, input().split())
    m1 = max(map(int, input().split()))
    m2 = max(map(int, input().split()))
    if m1 > m2:
        print("YES")
    else:
        print("NO")
