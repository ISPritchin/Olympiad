A, B = map(int, input().split())
x, y, z = map(int, input().split())
nA = 2*x+y
nB = 3*z+y
r = 0
if nA > A:
    r += nA-A
if nB > B:
    r += nB-B
print(r)
