s = input()
n_a = s.count("a")
ls = len(s)
n_not_a = ls - n_a
if n_a > n_not_a:
    print(ls)
else:
    print(n_a*2-1)
