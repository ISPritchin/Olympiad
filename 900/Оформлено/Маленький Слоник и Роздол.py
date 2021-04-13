n = int(input())
a = list(map(int, input().split()))
m = min(a)
if a.count(m) == 1:
    print(a.index(m) + 1)
else:
    print("Still Rozdil")
