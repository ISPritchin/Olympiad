def get_order(s):
    s.sort()
    r = []
    if len(s) % 2 == 1:
        left = len(s) // 2
        r.append(s[left])
        left -= 1
        right = left + 2
    else:
        right = len(s) // 2
        left = right -1
    while left != -1:
        r.append(s[left])
        left -= 1
        r.append(s[right])
        right += 1
    return r


n_sets = int(input())
for _ in range(n_sets):
    n = int(input())
    s = list(map(int, input().split()))
    s = get_order(s)
    print(*s)