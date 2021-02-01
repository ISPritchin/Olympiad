a, b, c = map(int, input().split())
a1 = c*2
a2 = min(a, b)*2
a3 = int(b > min(a, b) or a > min(a, b))
print(a1 + a2 + a3)
