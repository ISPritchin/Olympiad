# https://codeforces.com/problemset/problem/110/A

n = input()
c = sum([1 for x in n if x == "7" or x == "4"])
if c == 4 or c == 7:
    print("YES")
else:
    print("NO")
