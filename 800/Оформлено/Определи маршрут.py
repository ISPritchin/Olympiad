n = int(input())

_, *s = map(int, input().split())
s = set(s)
for i in range(n-1):
    _, *s2 = map(int, input().split())
    s &= set(s2)
for x in s:
    print(x, end=" ")