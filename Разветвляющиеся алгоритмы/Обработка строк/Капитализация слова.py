# https://codeforces.com/problemset/problem/281/A

w = input()
if ord("A") <= ord(w[0]) <= ord("Z"):
    print(w)
else:
    print(chr(ord(w[0]) + ord("A") - ord("a")) + w[1:])
