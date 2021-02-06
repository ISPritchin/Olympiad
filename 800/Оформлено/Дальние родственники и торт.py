def f(n):
    return n*(n-1) // 2

n = int(input())
ss = []
rx = []
for i in range(n):
    s = input()
    x = s.count("C")
    rx.append(x)
    ss.append(s)

cx = []
for j in range(n):
    c = 0
    for i in range(n):
        if ss[i][j] == "C":
            c += 1
    cx.append(c)

r = 0
for x in rx:
    if x != 0:
        r += f(x)
for x in cx:
    if x != 0:
        r += f(x)
print(r)
