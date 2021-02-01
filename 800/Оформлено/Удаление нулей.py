n_sets = int(input())
for _ in range(n_sets):
    s = input()
    left = s.find('1')
    right = s.rfind('1')
    if left == right:
        print(0)
    else:
        print(s[left + 1:right].count('0'))
