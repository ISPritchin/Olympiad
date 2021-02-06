from collections import Counter

n = int(input())
s = input()
ds = []
for i in range(1, len(s)):
    ds.append(s[i-1: i+1])
print(Counter(ds).most_common(1)[0][0])