name = input()
n = len(set([c for c in name]))
if n % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
