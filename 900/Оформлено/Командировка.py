n = int(input())
a = list(map(int, input().split()))
if sum(a) < n:
    print(-1)
elif n == 0:
    print(0)
else:
    a.sort(reverse=True)
    dk = 0
    for i in range(n):
        dk += a[i]
        if dk >= n:
            print(i+1)
            break
