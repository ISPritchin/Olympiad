n = int(input())
a = [0, 0] + list(map(int, input().split()))
b = []

i = n
while a[i] != 0:
    b.append(i)
    i = a[i]
b.append(1)
print(*b[::-1])
