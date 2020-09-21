# https://codeforces.com/contest/431/submission/91470520

a = [int(x) for x in input().split()]
s = map(int, list(input()))
print(sum([a[i-1] for i in s]))
