n_sets = int(input())
for i in range(n_sets):
    a, b, n, S = map(int, input().split())
    b_part = a * n
    if b_part >= S:
        S -= (S // n) * n
    else:
        S -= a * n
    if S <= b:
        print("YES")
    else:
        print("NO")
