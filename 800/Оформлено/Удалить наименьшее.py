n = int(input())
for i in range(n):
    n = int(input())
    a = [int(x) for x in input().split()]
    a = list(set(a))
    if max(a) - min(a) + 1 <= len(a):
        print("YES")
    else:
        print("NO")
