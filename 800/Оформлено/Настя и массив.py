n = int(input())
s = set(list(map(int, input().split())))
s = s.difference([0])
print(len(s))
