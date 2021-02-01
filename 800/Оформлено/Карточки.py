n = int(input())
s = list(input())
kz, ke, kr, ko, kn = s.count("z"), s.count("e"), s.count("r"), s.count("o"), s.count("n")
m = min(ko, kn, ke)
ko -= m
kn -= m
ke -= m
n = min(kz, ke, kr, ko)
for i in range(m):
    print(1, end=' ')
for i in range(n):
    print(0, end=' ')