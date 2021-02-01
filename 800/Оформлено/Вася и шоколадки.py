n_sets = int(input())
for _ in range(n_sets):
    s, a, b, c = map(int, input().split())
    n = s // c
    n = n // a * (a+b) + n % a
    print(n)
