n, m = map(int, input().split())
a = map(int, input().split())
b = list(map(int, input().split()))
for x in a:
    if x in b:
        print(x, end=' ')

