n = int(input())
arr = sorted(list(map(int, input().split())))
n_keyborrds = max(arr) - min(arr) + 1
print(n_keyborrds - n)
