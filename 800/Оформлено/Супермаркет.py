n, m = map(int, input().split())
p_res = float("inf")
for i in range(n):
    a, b = map(int, input().split())
    p = a / b
    if p < p_res:
        p_res = p
print(p_res*m)
