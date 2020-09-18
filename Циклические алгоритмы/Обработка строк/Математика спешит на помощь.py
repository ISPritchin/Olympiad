# https://codeforces.com/problemset/problem/339/A

s = input()
numbers = [c for c in s[::2]]
numbers.sort()
print("+".join(numbers))
