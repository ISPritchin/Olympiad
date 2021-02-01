a = list(map(int, input().split()))
a.sort()
a, b, c = a
if c < a + b:
    print(0)
else:
    print(c-a-b+1)
