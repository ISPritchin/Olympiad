from collections import Counter

n = int(input())
arr = map(int, input().split())
print(Counter(arr).most_common(1)[0][1])
