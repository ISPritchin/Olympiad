n = int(input())
for _ in range(n):
    s = input()
    nc = len(s)
    print(nc - s.count("0"))
    for i, x in enumerate(s):
        if x != '0':
            print(x + "0"*(nc-1-i), end=" ")
