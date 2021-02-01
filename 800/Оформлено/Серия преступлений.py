n, _ = map(int, input().split())

for i, _ in enumerate(range(n), 1):
    s = input()
    n = s.count("*")
    if n == 2:
        left = s.find("*")
        right = s.rfind("*")
    elif n == 1:
        row_number = i
        row = s

if row[left] == "*":
    print(row_number, right + 1)
else:
    print(row_number, left + 1)
