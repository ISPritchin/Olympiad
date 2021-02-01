s = input().lower()
for c in s:
    if c not in ['a', 'e', 'y', 'u', 'i', 'o']:
        print(f".{c}", end="")