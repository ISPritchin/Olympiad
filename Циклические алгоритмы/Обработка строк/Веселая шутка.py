# https://codeforces.com/problemset/problem/141/A

def word_to_list(s):
    w = [0] * 26
    for x in s:
        w[ord(x) - ord("A")] += 1
    return w


a = input()
b = input()
c = input()
if word_to_list(a + b) == word_to_list(c):
    print("YES")
else:
    print("NO")
