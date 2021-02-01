n, m = map(int, input().split())
s = input().split()
t = input().split()
q = int(input())
for i in range(q):
    year = int(input())
    year -= 1
    a = s[year % n]
    b = t[year % m]
    print(a + b)
