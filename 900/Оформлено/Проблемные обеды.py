n, k = map(int, input().split())
max_pleasure = float("-inf")
for i in range(n):
    f, t = map(int, input().split())
    if t > k:
        pleasure = f - t + k
    else:
        pleasure = f
    max_pleasure = max(max_pleasure, pleasure)
print(max_pleasure)