def read_arr(f=int):
    if f:
        return [f(x) for x in input().split()]
    else:
        return [x for x in input().split()]


n, m = read_arr()
r = set()
for i in range(n):
    row = set(read_arr(None))
    r |= row


for x in r:
    if x not in set(["B", "W", "G"]):
        print("#Color")
        break
else:
    print("#Black&White")
