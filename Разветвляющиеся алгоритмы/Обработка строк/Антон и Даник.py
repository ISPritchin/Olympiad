# https://codeforces.com/problemset/problem/734/A

n = int(input())
s = input()
nA = s.count("A")
nD = n - nA
if nA > nD:
    print("Anton")
elif nA < nD:
    print("Danik")
else:
    print("Friendship")
