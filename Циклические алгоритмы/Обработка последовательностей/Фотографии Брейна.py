# https://codeforces.com/contest/707/submission/91159033


def read_arr(f=None):
    if f:
        return [f(x) for x in input().split()]
    else:
        return [x for x in input().split()]


n, m = read_arr(int)
r = set()
for i in range(n):
    row = set(read_arr())
    r |= row

for color in r:
    if color not in ["B", "W", "G"]:
        print("#Color")
        break
else:
    print("#Black&White")
