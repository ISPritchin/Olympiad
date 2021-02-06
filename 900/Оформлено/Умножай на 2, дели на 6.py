n_sets = int(input())
for _ in range(n_sets):
    x = int(input())
    n2 = 0
    while x % 2 == 0:
        n2 += 1
        x //= 2
    n3 = 0
    while x % 3 == 0:
        n3 += 1
        x //= 3
        
    if x != 1 or n3 < n2:
        print(-1)
    else:
        c = min(n2, n3)
        n3 -= c
        n2 -= c
        print(c + n3*2)