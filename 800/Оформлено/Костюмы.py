a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

if e > f:
    n1 = min(a, d)
    a -= n1
    d -= n1
    n2 = min(b, c, d)
    b -= n2
    c -= n2
    d -= n2
    print(n1*e + n2*f)
else:
    n2 = min(b, c, d)
    b -= n2
    c -= n2
    d -= n2
    n1 = min(a, d)
    a -= n1
    d -= n1
    print(n1*e + n2*f)
