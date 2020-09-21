# https://codeforces.com/problemset/problem/151/A

n, k, l, c, d, p, nl, np = [int(x) for x in input().split()]
n_gas = k*l
n_laim = c*d
n_sol = p
print(min(n_laim, n_gas // nl, n_sol // np) // n)
