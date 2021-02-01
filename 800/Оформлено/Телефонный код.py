n = int(input())
max_prefix = input()
j = len(max_prefix)

for i in range(1, n):
    s = input()
    k = 0
    while s[k] == max_prefix[k] and k < j:
        k += 1
    j = k
print(k)